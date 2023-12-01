import numpy as np
import pytest
from tests.test_utils import run_clip_tests
from soundata import annotations
from soundata.datasets import dcase23_task4b
import os

TEST_DATA_HOME = os.path.normpath("tests/resources/sound_datasets/dcase23_task4b")


def test_clip():
    default_clipid = "cafe_restaurant_14"
    dataset = dcase23_task4b.Dataset(TEST_DATA_HOME)
    clip = dataset.clip(default_clipid)

    expected_attributes = {
        "audio_path": (
            os.path.join(
                os.path.normpath("tests/resources/sound_datasets/dcase23_task4b/"),
                "development_audio/cafe_restaurant/cafe_restaurant_14.wav",
            )
        ),
        "annotations_path": (
            os.path.join(
                os.path.normpath("tests/resources/sound_datasets/dcase23_task4b/"),
                "development_annotation/soft_labels_cafe_restaurant/cafe_restaurant_14.txt",
            )
        ),
        "clip_id": "cafe_restaurant_14",
    }

    expected_property_types = {
        "split": str,
        "audio": tuple,
        "events": annotations.Events,
        "non_verified_events": annotations.Events,
    }

    run_clip_tests(clip, expected_attributes, expected_property_types)


def test_load_audio():
    dataset = dcase23_task4b.Dataset(TEST_DATA_HOME)
    clip = dataset.clip("cafe_restaurant_14")
    audio_path = clip.audio_path
    audio, sr = dcase23_task4b.load_audio(audio_path)
    assert sr == 44100
    assert type(audio) is np.ndarray
    assert len(audio.shape) == 2  # check audio is loaded as stereo
    assert audio.shape[1] == 220500  # Check audio duration is as expected


def test_load_events():
    dataset = dcase23_task4b.Dataset(TEST_DATA_HOME)
    clip = dataset.clip("cafe_restaurant_14")
    annotations_path = clip.annotations_path
    annotations = dcase23_task4b.load_events(annotations_path)
    confidence = [0.22607917138849756, 0.12977944582818704, 0.3863415649633261]
    intervals = [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0]]
    labels = ["cutlery and dishes", "footsteps", "furniture dragging"]
    assert np.allclose(confidence, annotations.confidence)
    assert np.allclose(intervals, annotations.intervals)

    for j in range(3):
        assert labels[j] == annotations.labels[j]


def test_to_jams():
    default_clipid = "cafe_restaurant_14"
    dataset = dcase23_task4b.Dataset(TEST_DATA_HOME)
    clip = dataset.clip(default_clipid)
    jam = clip.to_jams()

    assert jam.validate()

    # Validate Events
    events = jam.search(namespace="segment_open")[0]["data"]
    assert len(events) == 3

    assert np.allclose(events[0].time, 0.0)
    assert np.allclose(events[0].duration, 1.0 - 0.0)
    assert events[0].value == "cutlery and dishes"
    assert events[0].confidence == 0.22607917138849756

    assert np.allclose(events[1].time, 0.0)
    assert np.allclose(events[1].duration, 1.0 - 0.0)
    assert events[1].value == "footsteps"
    assert events[1].confidence == 0.12977944582818704

    assert np.allclose(events[2].time, 0.0)
    assert np.allclose(events[2].duration, 1.0 - 0.0)
    assert events[2].value == "furniture dragging"
    assert events[2].confidence == 0.3863415649633261

    # Validate metadata
    assert jam.file_metadata.duration == 5.0
    assert jam.sandbox.split == "development"
    assert jam.annotations[0].annotation_metadata.data_source == "soundata"

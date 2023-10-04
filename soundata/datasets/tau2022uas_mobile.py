"""TAU Urban Acoustic Scenes 2022 Mobile Loader

.. admonition:: Dataset Info
    :class: dropdown

    **TAU Urban Acoustic Scenes 2022 Mobile, Development and Evaluation
    datasets**

    `Audio Research Group,
    Tampere University of Technology <http://arg.cs.tut.fi/>`_

    Authors

    * `Toni Heittola <http://www.cs.tut.fi/~heittolt/>`_
    * `Annamaria Mesaros <http://www.cs.tut.fi/~mesaros/>`_
    * `Tuomas Virtanen <http://www.cs.tut.fi/~tuomasv/>`_

    Recording and annotation

    * Henri Laakso
    * Ronal Bejarano Rodriguez
    * Toni Heittola


    Links

    * `Development dataset <https://zenodo.org/record/6337421>`_
    * `Evaluation dataset <https://zenodo.org/record/7870258>`_

    **Dataset**

    TAU Urban Acoustic Scenes 2022 Mobile development dataset consists of
    1-seconds audio segments from 10 acoustic scenes:

    * Airport - `airport`
    * Indoor shopping mall - `shopping_mall`
    * Metro station - `metro_station`
    * Pedestrian street - `street_pedestrian`
    * Public square - `public_square`
    * Street with medium level of traffic - `street_traffic`
    * Travelling by a tram - `tram`
    * Travelling by a bus - `bus`
    * Travelling by an underground metro - `metro`
    * Urban park - `park`

    The dataset contains the same material than TAU Urban Acoustic Scenes 2020 Mobile development dataset, 
    10-second audio segments have been split into non-overlapping 1-second segments for 2022 version of the dataset.

    A detailed description of the data recording and annotation procedure is
    available in:

    .. code-block:: latex

        Annamaria Mesaros, Toni Heittola, and Tuomas Virtanen.
        "Acoustic scene classification in DCASE 2020 Challenge:
        generalization across devices and low complexity solutions",
        In Proceedings of the Detection and Classification of Acoustic
        Scenes and Events 2020 Workshop (DCASE2020), Tokyo, Japan, 2020.

    Recordings were made with three devices (A, B and C) that captured audio
    simultaneously and 6 simulated devices (S1-S6). Each acoustic scene has
    1440 segments (240 minutes of audio) recorded with device A (main device)
    and 108 segments of parallel audio (18 minutes) each recorded with devices
    B,C, and S1-S6.

    *Development dataset*

    The dataset contains in total 64 hours of audio.

    *Evaluation dataset*

    The dataset contains in total 33 hours of audio.


    The dataset was collected by Tampere University of Technology between
    05/2018 -11/2018. The data collection has received funding from
    the European Research Council under the `ERC <https://erc.europa.eu/1>`_
    Grant Agreement 637422 EVERYSOUND.


    **Preparation of the dataset**

    The dataset was recorded in 12 large European cities: Amsterdam, Barcelona,
    Helsinki, Lisbon, London, Lyon, Madrid, Milan, Prague, Paris, Stockholm,
    and Vienna. For all acoustic scenes, audio was captured in multiple
    locations: different streets, different parks, different shopping malls.
    In each location, multiple 2-3 minute long audio recordings were captured
    in a few slightly different positions (2-4) within the selected location.
    Collected audio material was cut into segments of 10 seconds length. 

    The main recording device (referred to as device A) consists of a binaural
    `Soundman OKM IIKlassik/studio A3 <http://www.soundman.de/en/products/>`_
    electret in-ear microphone and a `Zoom F8
    <https://www.zoom.co.jp/products/handy-recorder/zoom-f8-multitrack-field-recorder>`_
    audio recorder using 48 kHz sampling rate and 24 bit resolution. During the
    recording, the microphones were worn by the recording person in the ears,
    and head movement was kept to minimum.

    Devices B and C are commonly available customer devices (e.g. smartphones,
    cameras) and were handled in typical ways (e.g. hand held). The audio
    recordings from these devices are of different quality than device A. All
    simultaneous recordings are time synchronized.

    Post-processing of the recorded audio involves aspects related to privacy
    of recorded individuals, and possible errors in the recording process.
    The material was screened for content, and segments containing close
    microphone conversation were eliminated. Some interferences from mobile
    phones are audible, but are considered part of real-world recording
    process. In addition, data from device A was resampled and averaged into a
    single channel, to align with the properties of the data recorded with
    devices B and C.

    Additionally, 11 mobile devices S1-S11 are simulated using the audio
    recorded with device A, impulse responses recorded with real devices, and
    additional dynamic range compression, in order to simulate realistic
    recordings. A recording from device A is processed through convolution
    with the selected Si impulse response, then processed with a selected set
    of parameters for dynamic range compression (device specific). The impulse
    responses are proprietary data and will not be published.

    All provided audio data is single-channel, having a 44.1 KHz sampling rate,
    and 24 bit resolution.

    A subset of the dataset has been previously published as TUT Urban Acoustic
    Scenes 2019 Development dataset. Audio segment filenames are retained for
    the segments coming from this dataset.

    **Dataset statistics**

    The development set contains data from 10 cities and 9 devices: 3 real
    devices (A, B, C) and 6 simulated devices (S1-S6). Data from devices B, C
    and S1-S6 consists of randomly selected segments from the simultaneous
    recordings, therefore all overlap with the data from device A, but not
    necessarily with each other. The total amount of audio in the development
    set is **64 hours**. The evaluation dataset (TAU Urban Acoustic Scenes 2022
    Mobile evaluation) contains data from all 12 cities, and five new devices
    (not available in the development set): real device D and simulated devices
    S7-S11.

    **Device A**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              14400       1280        1490        1440       1450       1440       1440       1560       1440       1580        1280       
    Bus                  14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Metro                14400       1410        1440        1440       1460       1440       1440       1440       1440       1450        1440       
    Metro station        14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Park                 14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Public square        14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Shopping mall        14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Street, pedestrian   14400       1450        1450        1440       1450       1440       1440       1440       1440       1450        1400       
    Street, traffic      14400       1440        1440        1440       1440       1440       1440       1440       1440       1440        1440       
    Tram                 14400       1430        1450        1440       1440       1440       1440       1440       1440       1440        1440       
    **Total**            **144000**  **14210**   **14470**   **14400**  **14440**  **14400**  **14400**  **14520**  **14400**  **14560**   **14200**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              40          4           3           4          3          4          4          4          6          5           3         
    Bus                  71          4           4           11         7          7          7          11         10         6           4         
    Metro                67          3           5           11         4          9          8          9          10         4           4         
    Metro station        57          5           6           4          12         5          4          9          4          4           4         
    Park                 41          4           4           4          4          4          4          4          4          5           4         
    Public_square        43          4           4           4          4          5          4          4          6          4           4         
    Shopping mall        36          4           4           4          2          3          3          4          4          4           4         
    Street, pedestrian   46          7           4           4          4          4          5          5          5          4           4         
    Street, traffic      43          4           4           4          5          4          6          4          4          4           4         
    Tram                 70          4           4           6          9          7          11         9          11         5           4         
    **Total**            **514**     **43**      **42**      **56**     **54**     **52**     **56**     **63**     **65**     **45**      **39**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device B**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1070        110         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1070        110         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10780**   **1180**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              36          3           3           4          3          3          4          4          5          4           3         
    Bus                  57          4           4           9          7          6          5          8          7          3           4         
    Metro                47          3           4           6          4          6          5          6          6          4           4         
    Metro station        45          4           4           3          8          5          3          7          3          4           4         
    Park                 37          4           4           4          4          4          3          4          3          3           4         
    Public_square        37          3           4           4          4          5          3          4          4          3           3         
    Shopping mall        34          4           4           4          2          3          3          4          4          3           3         
    Street, pedestrian   43          6           3           4          4          4          5          5          4          4           4         
    Street, traffic      41          4           4           4          4          4          6          4          4          4           4         
    Tram                 50          4           4           5          6          5          5          7          7          3           4         
    **Total**            **427**     **39**      **37**      **47**     **46**     **44**     **42**     **53**     **47**     **35**      **37**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    
    **Device C**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1070        110         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1070        120         120         120        100        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1070        110         120         120        110        110        100        100        100        100         100       
    **Total**            **10770**   **1180**    **1200**    **1200**   **1090**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              38          4           3           4          3          3          4          4          5          5           3         
    Bus                  50          4           4           7          6          5          4          7          7          3           3         
    Metro                54          3           3           6          4          9          6          7          8          4           4         
    Metro station        48          5           3           4          8          5          4          7          4          4           4         
    Park                 39          4           4           4          4          4          4          4          4          3           4         
    Public_square        40          4           3           4          4          4          4          4          6          3           4         
    Shopping mall        35          4           4           4          2          3          3          4          4          3           4         
    Street, pedestrian   41          6           3           4          4          3          5          4          5          4           3         
    Street, traffic      40          4           3           4          4          4          6          4          4          4           3         
    Tram                 51          4           4           5          6          4          8          6          7          3           4         
    **Total**            **436**     **42**      **34**      **46**     **45**     **44**     **48**     **51**     **54**     **36**      **36**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device S1**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              37          4           3           4          3          4          4          4          4          4           3         
    Bus                  54          4           4           8          6          6          6          7          6          3           4         
    Metro                50          3           3           8          4          7          6          6          6          4           3         
    Metro station        48          5           4           4          9          5          4          5          4          4           4         
    Park                 36          4           4           4          4          3          4          3          3          3           4         
    Public_square        37          4           4           4          4          4          4          3          3          3           4         
    Shopping mall        33          4           4           4          2          3          3          3          3          3           4         
    Street, pedestrian   40          6           3           4          4          3          5          2          5          4           4         
    Street, traffic      40          4           4           4          4          4          6          3          3          4           4         
    Tram                 52          4           4           5          7          6          7          6          6          3           4         
    **Total**            **427**     **42**      **37**      **49**     **47**     **45**     **49**     **42**     **43**     **35**      **38**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device S2**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              36          3           3           4          3          4          4          4          4          4           3         
    Bus                  58          4           4           9          6          6          7          9          6          3           4         
    Metro                55          3           3           10         4          8          8          5          7          4           3         
    Metro station        49          5           4           4          7          5          4          8          4          4           4         
    Park                 38          4           4           4          4          4          4          4          4          2           4         
    Public_square        41          4           4           4          4          5          4          4          5          3           4         
    Shopping mall        34          4           4           3          2          3          3          4          4          3           4         
    Street, pedestrian   42          7           3           4          4          3          5          5          4          4           3         
    Street, traffic      42          4           4           4          5          4          6          4          4          4           3         
    Tram                 51          4           4           5          7          6          7          7          4          3           4         
    **Total**            **446**     **42**      **37**      **51**     **46**     **48**     **52**     **54**     **46**     **34**      **36**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device S3**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              36          3           3           4          3          4          4          4          4          4           3         
    Bus                  50          4           4           6          5          6          6          7          5          3           4         
    Metro                50          3           3           10         4          5          6          4          8          3           4         
    Metro station        44          4           4           4          6          5          4          7          3          4           3         
    Park                 39          4           4           4          4          4          4          4          4          3           4         
    Public_square        39          4           4           3          4          5          4          4          4          3           4         
    Shopping mall        32          4           4           3          2          3          3          4          3          3           3         
    Street, pedestrian   39          6           3           3          4          4          4          5          3          4           3         
    Street, traffic      40          4           4           4          5          4          5          4          3          3           4         
    Tram                 50          4           4           5          8          5          7          6          5          3           3         
    **Total**            **419**     **40**      **37**      **46**     **45**     **45**     **47**     **49**     **42**     **33**      **35**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device S4**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              36          3           3           4          3          4          4          4          4          4           3         
    Bus                  53          4           4           9          5          6          5          6          7          3           4         
    Metro                50          3           2           8          4          7          6          7          6          4           3         
    Metro station        47          5           4           4          7          5          4          6          4          4           4         
    Park                 38          4           3           4          4          4          4          4          4          3           4         
    Public_square        38          4           4           3          3          5          4          4          4          3           4         
    Shopping mall        35          4           4           4          2          3          3          4          4          3           4         
    Street, pedestrian   42          7           3           3          4          4          4          4          5          4           4         
    Street, traffic      41          4           4           4          4          4          5          4          4          4           4         
    Tram                 51          4           4           6          6          7          5          7          5          3           4         
    **Total**            **431**     **42**      **35**      **49**     **42**     **49**     **44**     **50**     **47**     **35**      **38**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
  
    **Device S5**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              38          4           3           4          3          4          4          3          5          5           3         
    Bus                  54          3           4           6          6          6          7          8          7          3           4         
    Metro                51          3           3           7          4          8          6          6          7          4           3         
    Metro station        45          5           3           3          7          4          4          7          4          4           4         
    Park                 36          3           4           3          3          4          4          4          4          3           4         
    Public_square        39          3           4           3          4          4          4          4          6          3           4         
    Shopping mall        33          3           4           3          2          3          3          4          4          3           4         
    Street, pedestrian   42          6           3           4          4          4          4          5          5          4           3         
    Street, traffic      38          3           3           4          4          4          4          4          4          4           4         
    Tram                 50          4           4           4          6          5          8          7          6          3           3         
    **Total**            **426**     **37**      **35**      **41**     **43**     **46**     **48**     **52**     **52**     **36**      **36**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    **Device S6**

    *Audio segments*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Segments    Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              1080        120         120         120        110        110        100        100        100        100         100       
    Bus                  1080        120         120         120        110        110        100        100        100        100         100       
    Metro                1080        120         120         120        110        110        100        100        100        100         100       
    Metro station        1080        120         120         120        110        110        100        100        100        100         100       
    Park                 1080        120         120         120        110        110        100        100        100        100         100       
    Public square        1080        120         120         120        110        110        100        100        100        100         100       
    Shopping mall        1080        120         120         120        110        110        100        100        100        100         100       
    Street, pedestrian   1080        120         120         120        110        110        100        100        100        100         100       
    Street, traffic      1080        120         120         120        110        110        100        100        100        100         100       
    Tram                 1080        120         120         120        110        110        100        100        100        100         100       
    **Total**            **10800**   **1200**    **1200**    **1200**   **1100**   **1100**   **1000**   **1000**   **1000**   **1000**    **1000**  
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========

    *Recording locations*

    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Scene class          Locations   Barcelona   Helsinki    Lisbon     London     Lyon       Milan      Paris      Prague     Stockholm   Vienna    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    Airport              36          4           3           4          3          4          3          3          5          4           3         
    Bus                  55          3           4           9          7          6          5          9          6          2           4         
    Metro                51          3           2           7          4          7          6          7          8          3           4         
    Metro station        47          5           4           4          9          3          3          7          4          4           4         
    Park                 37          3           4           4          4          4          3          4          4          3           4         
    Public_square        39          4           4           4          4          4          3          4          5          3           4         
    Shopping mall        33          3           4           4          2          3          2          4          4          3           4         
    Street, pedestrian   39          5           3           4          4          3          4          4          4          4           4         
    Street, traffic      39          3           4           3          4          4          5          4          4          4           4         
    Tram                 56          4           4           6          7          6          7          6          9          3           4         
    **Total**            **432**     **37**      **35**      **49**     **48**     **44**     **41**     **52**     **53**     **33**      **39**    
    ===================  ==========  ==========  ==========  =========  ========= ==========  =========  =========  =========  ==========  ==========
    
    **Usage**

    The partitioning of the data was done based on the location of the original
    recordings. All segments recorded at the same location were included into a
    single subset - either **development dataset** or **evaluation dataset**.
    For each acoustic scene, 1440 segments recorded with device A, 108 segments
    recorded with device B, C and S1-S6 were included in the development
    dataset provided here. Evaluation dataset is provided separately.

    *Training / test setup*

    A suggested training/test partitioning of the development set is provided
    in order to make results reported with this dataset uniform. The
    partitioning is done such that the segments recorded at the same location
    are included into the same subset - either training or testing. The
    partitioning is done aiming for a 70/30 ratio between the number of
    segments in training and test subsets while taking into account recording
    locations, and selecting the closest available option.

    Data from devices A, B, C, S1, S2, S3 are available in both training and
    test sets. Audio segments coming from devices S4, S5, and S6 are used only
    for testing. Since the dataset includes balanced amount of material from
    devices (B, C, and S1-S6), this partitioning will leave a small subset of
    data from devices S4-S6 unused in the training / test setup. This material
    can be used when using full dataset to train the system and testing it with
    evaluation dataset.

    The setup is provided with the dataset in the directory `evaluation_setup`. 

    *Statistics*

    ===================  =================  ==================  ================  =================  ==================  =================== 
    Scene class          Train / Segments   Train / Locations   Test / Segments   Test / Locations   Unused / Segments   Unused / Locations  
    ===================  =================  ==================  ================  =================  ==================  ===================
    Airport              13930               28                  2960               12                 6130                 40                  
    Bus                  14000               51                  2970               19                 6070                 66                  
    Metro                13820               47                  2970               20                 6250                 65                  
    Metro station        13800               40                  2970               16                 6270                 55                  
    Park                 14290               30                  2970               11                 5780                 39                  
    Public square        14270               31                  2970               12                 5790                 42                  
    Shopping mall        13730               26                  2970               10                 6330                 35                  
    Street, pedestrian   13860               32                  2970               14                 6210                 45                  
    Street, traffic      14130               31                  2970               12                 5940                 43                  
    Tram                 13790               49                  2960               20                 6280                 67                  
    **Total**            **139620**          **365**             **29680**          **146**            **610500**            **497**             
    ===================  =================  ==================  ================  =================  ==================  ===================

    *Number of segments in train / test setup*

    ===================  =================  ==================  ================  =================  ==================  ===================
    Scene class          Train / Device A   Train / Device B,C,S1-S3   Test / Device A   Test / Device Device B,C,S1-S3   Test / Device S4-S6  
    ===================  =================  ==================  ================  =================  ==================  ===================
    Airport              10190              750                        330               330                              330                  
    Bus                  10250              750                        330               330                              330                  
    Metro                10070              750                        330               330                              330                  
    Metro station        10050              750                        330               330                              330                  
    Park                 10540              750                        330               330                              330                  
    Public square        10530              750                        330               330                              330                  
    Shopping mall        9990               750                        330               330                              330                  
    Street, pedestrian   10110              750                        330               330                              330                  
    Street, traffic      10380              750                        330               330                              330                  
    Tram                 10040              750                        330               330                              330                  
    **Total**            102150             **7500**                   **3300**          **16500**                        **9900**             
    ===================  =================  ==================  ================  =================  ==================  ===================

    **License**
    
    License permits free academic usage. Any commercial use is strictly prohibited. For commercial use, contact dataset authors.

        Copyright (c) 2022 Tampere University and its licensors
        All rights reserved.
        Permission is hereby granted, without written agreement and without license or royalty
        fees, to use and copy the TAU Urban Acoustic Scenes 2022 Mobile (“Work”) described in this document
        and composed of audio and metadata. This grant is only for experimental and non-commercial
        purposes, provided that the copyright notice in its entirety appear in all copies of this Work,
        and the original source of this Work, (Audio Research Group at Tampere University of Technology),
        is acknowledged in any publication that reports research using this Work.
        Any commercial use of the Work or any part thereof is strictly prohibited.
        Commercial use include, but is not limited to:
        - selling or reproducing the Work
        - selling or distributing the results or content achieved by use of the Work
        - providing services by using the Work.

        IN NO EVENT SHALL TAMPERE UNIVERSITY OR ITS LICENSORS BE LIABLE TO ANY PARTY
        FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE
        OF THIS WORK AND ITS DOCUMENTATION, EVEN IF TAMPERE UNIVERSITY OR ITS
        LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        TAMPERE UNIVERSITY AND ALL ITS LICENSORS SPECIFICALLY DISCLAIMS ANY
        WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
        FITNESS FOR A PARTICULAR PURPOSE. THE WORK PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND
        THE TAMPERE UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT,
        UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
"""

import os
from typing import BinaryIO, Optional, TextIO, Tuple

import librosa
import numpy as np
import csv

from soundata import download_utils, jams_utils, core, annotations, io


BIBTEX = """
@inproceedings{Heittola:DCASE:20,
    Address = {Tokyo, Japan},
    Author = {Mesaros, A. and Heittola, T. and Virtanen, T.},
    Booktitle = {Proceedings of the Detection and Classification of Acoustic
                 Scenes and Events 2020 Workshop (DCASE2020},
    Month = {November},
    Pages = {56--60},
    Title = {Acoustic scene classification in DCASE 2020 Challenge:
    generalization across devices and low complexity solutions},
    Year = {2020}}
"""
REMOTES = {
    "development.audio.1": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.1.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.1.zip?download=1",
        checksum="b1e85b8a908d3d6a6ab73268f385d5c8",
    ),
    "development.audio.2": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.2.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.2.zip?download=1",
        checksum="4310a13cc2943d6ce3f70eba7ba4c784",
    ),
    "development.audio.3": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.3.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.3.zip?download=1",
        checksum="ed38956c4246abb56190c1e9b602b7b8",
    ),
    "development.audio.4": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.4.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.4.zip?download=1",
        checksum="97ab8560056b6816808dedc044dcc023",
    ),
    "development.audio.5": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.5.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.5.zip?download=1",
        checksum="b50f5e0bfed33cd8e52cb3e7f815c6cb",
    ),
    "development.audio.6": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.6.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.6.zip?download=1",
        checksum="fbf856a3a86fff7520549c899dc94372",
    ),
    "development.audio.7": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.7.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.7.zip?download=1",
        checksum="0dbffe7b6e45564da649378723284062",
    ),
    "development.audio.8": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.8.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.8.zip?download=1",
        checksum="bb6f77832bf0bd9f786f965beb251b2e",
    ),
    "development.audio.9": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.9.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.9.zip?download=1",
        checksum="a65596a5372eab10c78e08a0de797c9e",
    ),
    "development.audio.10": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.10.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.10.zip?download=1",
        checksum="2ad595819ffa1d56d2de4c7ed43205a6",
    ),
    "development.audio.11": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.11.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.11.zip?download=1",
        checksum="0ad29f7040a4e6a22cfd639b3a6738e5",
    ),
    "development.audio.12": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.12.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.12.zip?download=1",
        checksum="e5f4400c6b9697295fab4cf507155a2f",
    ),
    "development.audio.13": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.13.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.13.zip?download=1",
        checksum="8855ab9f9896422746ab4c5d89d8da2f",
    ),
    "development.audio.14": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.14.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.14.zip?download=1",
        checksum="092ad744452cd3e7de78f988a3d13020",
    ),
    "development.audio.15": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.15.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.15.zip?download=1",
        checksum="4b5eb85f6592aebf846088d9df76b420",
    ),
    "development.audio.16": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.audio.16.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.audio.16.zip?download=1",
        checksum="2e0a89723e58a3836be019e6996ae460",
    ),
    "development.doc": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.doc.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.doc.zip?download=1",
        checksum="175f40dc3fec144347abad4d2962b7ae",
    ),
    "development.meta": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2022-mobile-development.meta.zip",
        url="https://zenodo.org/record/6337421/files/TAU-urban-acoustic-scenes-2022-mobile-development.meta.zip?download=1",
        checksum="6eae9db553ce48e4ea246e34e50a3cf5",
    ),
    "evaluation.audio.1": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.1.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.1.zip?download=1",
        checksum="632841f6b1ef9ed962ea61f879967411",
    ),
    "evaluation.audio.2": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.2.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.2.zip?download=1",
        checksum="711fb0469f9b66669a300ebd1de24e9b",
    ),
    "evaluation.audio.3": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.3.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.3.zip?download=1",
        checksum="575e517b826a5faf020be22ce766adf8",
    ),
    "evaluation.audio.4": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.4.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.4.zip?download=1",
        checksum="5919fcbe217964756892a9661323c020",
    ),
    "evaluation.audio.5": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.5.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.5.zip?download=1",
        checksum="c733767217f16c746f50796c65ca1dd6",
    ),
    "evaluation.audio.6": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.6.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.6.zip?download=1",
        checksum="f39feb24910ffc97413e9c94b418f7ab",
    ),
    "evaluation.audio.7": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.7.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.7.zip?download=1",
        checksum="90bad61f14163146702d430cf8241932",
    ),
    "evaluation.audio.8": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.8.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.audio.8.zip?download=1",
        checksum="4db5255382a5e5cab2d463c0d836b888",
    ),
    "evaluation.doc": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.doc.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.doc.zip?download=1",
        checksum="2f1ac2991111c6ee1d51bec6e27bd825",
    ),
    "evaluation.meta": download_utils.RemoteFileMetadata(
        filename="TAU-urban-acoustic-scenes-2023-mobile-evaluation.meta.zip",
        url="https://zenodo.org/record/7870258/files/TAU-urban-acoustic-scenes-2023-mobile-evaluation.meta.zip?download=1",
        checksum="b8d9bb50faa282be170b81dc57e2b8b3",
    ),
}


LICENSE_INFO = """
    License permits free academic usage. Any commercial use is strictly prohibited. For commercial use, contact dataset authors.

        Copyright (c) 2022 Tampere University and its licensors
        All rights reserved.
        Permission is hereby granted, without written agreement and without license or royalty
        fees, to use and copy the TAU Urban Acoustic Scenes 2022 Mobile (“Work”) described in this document
        and composed of audio and metadata. This grant is only for experimental and non-commercial
        purposes, provided that the copyright notice in its entirety appear in all copies of this Work,
        and the original source of this Work, (Audio Research Group at Tampere University of Technology),
        is acknowledged in any publication that reports research using this Work.
        Any commercial use of the Work or any part thereof is strictly prohibited.
        Commercial use include, but is not limited to:
        - selling or reproducing the Work
        - selling or distributing the results or content achieved by use of the Work
        - providing services by using the Work.

        IN NO EVENT SHALL TAMPERE UNIVERSITY OR ITS LICENSORS BE LIABLE TO ANY PARTY
        FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE
        OF THIS WORK AND ITS DOCUMENTATION, EVEN IF TAMPERE UNIVERSITY OR ITS
        LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

        TAMPERE UNIVERSITY AND ALL ITS LICENSORS SPECIFICALLY DISCLAIMS ANY
        WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
        FITNESS FOR A PARTICULAR PURPOSE. THE WORK PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND
        THE TAMPERE UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT,
        UPDATES, ENHANCEMENTS, OR MODIFICATIONS.
"""


class Clip(core.Clip):
    """TAU Urban Acoustic Scenes 2022 Mobile Clip class

    Args:
        clip_id (str): id of the clip

    Attributes:
        audio (np.ndarray, float): path to the audio file
        audio_path (str): path to the audio file
        city (str): city were the audio signal was recorded
        clip_id (str): clip id
        identifier (str): the clip identifier
        source_label (str): source label
        split (str): subset the clip belongs to (for experiments):
            development (fold1, fold2, fold3, fold4) or evaluation
        tags (soundata.annotations.Tags): tag (label) of the clip + confidence
    """

    def __init__(self, clip_id, data_home, dataset_name, index, metadata):
        super().__init__(clip_id, data_home, dataset_name, index, metadata)

        self.audio_path = self.get_path("audio")

    @property
    def audio(self) -> Optional[Tuple[np.ndarray, float]]:
        """The clip's audio

        Returns:
            * np.ndarray - audio signal
            * float - sample rate

        """
        return load_audio(self.audio_path)

    @property
    def split(self):
        """The clip's split.

        Returns:
            * str - subset the clip belongs to (for experiments): development (fold1, fold2, fold3, fold4) or evaluation

        """
        return self._clip_metadata.get("split")

    @property
    def tags(self):
        """The clip's tags.

        Returns:
            * annotations.Tags - tag (label) of the clip + confidence

        """
        scene_label = self._clip_metadata.get("scene_label")
        if scene_label is None:
            return None
        else:
            return annotations.Tags([scene_label], "open", np.array([1.0]))

    @property
    def city(self):
        """The clip's city.

        Returns:
            * str - city were the audio signal was recorded

        """
        return self._clip_metadata.get("city")

    @property
    def source_label(self):
        """The clip's source label.

        Returns:
            * str - source label

        """
        return self._clip_metadata.get("source_label")

    @property
    def identifier(self):
        """The clip's identifier.

        Returns:
            * str - clip identifier

        """
        return self._clip_metadata.get("identifier")

    def to_jams(self):
        """Get the clip's data in jams format

        Returns:
            jams.JAMS: the clip's data in jams format

        """
        return jams_utils.jams_converter(
            audio_path=self.audio_path, tags=self.tags, metadata=self._clip_metadata
        )


@io.coerce_to_bytes_io
def load_audio(fhandle: BinaryIO, sr=None) -> Tuple[np.ndarray, float]:
    """Load a TAU Urban Acoustic Scenes 2022 Mobile audio file.

    Args:
        fhandle (str or file-like): File-like object or path to audio file
        sr (int or None): sample rate for loaded audio, None by default, which
            uses the file's original sample rate of 44100 without resampling.

    Returns:
        * np.ndarray - the mono audio signal
        * float - The sample rate of the audio file

    """
    audio, sr = librosa.load(fhandle, sr=sr, mono=True)
    return audio, sr


@core.docstring_inherit(core.Dataset)
class Dataset(core.Dataset):
    """
    The TAU Urban Acoustic Scenes 2022 Mobile dataset
    """

    def __init__(self, data_home=None):
        super().__init__(
            data_home,
            name="tau2022uas_mobile",
            clip_class=Clip,
            bibtex=BIBTEX,
            remotes=REMOTES,
            license_info=LICENSE_INFO,
        )

    @core.copy_docs(load_audio)
    def load_audio(self, *args, **kwargs):
        return load_audio(*args, **kwargs)

    @core.cached_property
    def _metadata(self):
        metadata_path = os.path.join(
            self.data_home,
            "TAU-urban-acoustic-scenes-2022-mobile-development",
            "meta.csv",
        )

        splits = ["development.train", "development.evaluate", "evaluation"]

        metadata_index = {}

        with open(metadata_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for row in csv_reader:
                file_name = os.path.basename(row[0])
                clip_id = os.path.basename(file_name).replace(".wav", "")
                scene_label = row[1]
                identifier = row[2]
                source_label = row[3]
                city = identifier.split("-")[0]
                metadata_index[clip_id] = {
                    "scene_label": scene_label,
                    "city": city,
                    "identifier": identifier,
                    "source_label": source_label,
                }

        for split in splits:
            subset = split.split(".")[0]
            evaluation_setup_path = (
                "TAU-urban-acoustic-scenes-2022-mobile-{}/evaluation_setup".format(
                    subset
                )
            )
            if subset == "development":
                fold = split.split(".")[1]
                evaluation_setup_file = os.path.join(
                    self.data_home, evaluation_setup_path, "fold1_{}.csv".format(fold)
                )
            else:
                evaluation_setup_file = os.path.join(
                    self.data_home, evaluation_setup_path, "fold1_test.csv"
                )

            with open(evaluation_setup_file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter="\t")
                next(csv_reader)
                for row in csv_reader:
                    file_name = os.path.basename(row[0])
                    clip_id = os.path.basename(file_name).replace(".wav", "")

                    if subset != "development":
                        metadata_index[clip_id] = {
                            "scene_label": None,
                            "city": None,
                            "identifier": None,
                            "source_label": None,
                        }

                    metadata_index[clip_id]["split"] = split

        return metadata_index

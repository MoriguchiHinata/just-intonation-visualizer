import numpy as np
import math


def get_freqs(pitch_root_tuple):
    root_name = ""
    est_freqs = []

    # 根音を探す
    for pitch, is_root in pitch_root_tuple:
        if is_root:
            root_name = pitch
            break

    # 根音が設定されていない場合
    if root_name == "":
        print("ERROR: 根音が設定されていません")
        return []

    # 根音を基準に純正律の周波数を計算
    root_idx = pitchname_list.index(root_name)

    for pitch, _ in pitch_root_tuple:
        # pitchname_list.index(pitch) - root_idx で根音から何半音離れているか計算
        # 12半音周期で根音に純正律の比率をかける

        semitone_distance = pitchname_list.index(pitch) - root_idx

        if semitone_distance > 0:
            est_freqs.append(
                freq_dict[root_name]
                * just_ratios[semitone_distance % 12]
                * (2 ** (semitone_distance // 12))  # オクターブ違いに対応
            )
        else:
            est_freqs.append(
                freq_dict[root_name]
                * (just_ratios[semitone_distance % 12])
                * (2 ** math.ceil(semitone_distance // 12))  # オクターブ違いに対応
            )

    print(est_freqs)

    return est_freqs


# 純正律をつくる比率
just_ratios = [
    1,
    16 / 15,
    9 / 8,
    6 / 5,
    5 / 4,
    4 / 3,
    45 / 32,
    3 / 2,
    8 / 5,
    5 / 3,
    16 / 9,
    15 / 8,
]

pitchname_list = [
    "C1",
    "C#1",
    "D1",
    "D#1",
    "E1",
    "F1",
    "F#1",
    "G1",
    "G#1",
    "A1",
    "A#1",
    "B1",
    "C2",
    "C#2",
    "D2",
    "D#2",
    "E2",
    "F2",
    "F#2",
    "G2",
    "G#2",
    "A2",
    "A#2",
    "B2",
    "C3",
    "C#3",
    "D3",
    "D#3",
    "E3",
    "F3",
    "F#3",
    "G3",
    "G#3",
    "A3",
    "A#3",
    "B3",
    "C4",
    "C#4",
    "D4",
    "D#4",
    "E4",
    "F4",
    "F#4",
    "G4",
    "G#4",
    "A4",
    "A#4",
    "B4",
    "C5",
    "C#5",
    "D5",
    "D#5",
    "E5",
    "F5",
    "F#5",
    "G5",
    "G#5",
    "A5",
    "A#5",
    "B5",
    "C6",
    "C#6",
    "D6",
    "D#6",
    "E6",
    "F6",
    "F#6",
    "G6",
    "G#6",
    "A6",
    "A#6",
    "B6",
]

freq_dict = {
    "C1": 32.70319566257483,
    "C#1": 34.64782887210901,
    "D1": 36.70809598967595,
    "D#1": 38.890872965260115,
    "E1": 41.20344461410874,
    "F1": 43.653528929125486,
    "F#1": 46.2493028389543,
    "G1": 48.99942949771866,
    "G#1": 51.91308719749314,
    "A1": 55.0,
    "A#1": 58.27047018976124,
    "B1": 61.735412657015516,
    "C2": 65.40639132514966,
    "C#2": 69.29565774421802,
    "D2": 73.4161919793519,
    "D#2": 77.78174593052023,
    "E2": 82.40688922821748,
    "F2": 87.30705785825097,
    "F#2": 92.4986056779086,
    "G2": 97.99885899543732,
    "G#2": 103.82617439498628,
    "A2": 110.0,
    "A#2": 116.54094037952248,
    "B2": 123.47082531403103,
    "C3": 130.8127826502993,
    "C#3": 138.59131548843604,
    "D3": 146.8323839587038,
    "D#3": 155.56349186104046,
    "E3": 164.81377845643496,
    "F3": 174.61411571650194,
    "F#3": 184.9972113558172,
    "G3": 195.99771799087463,
    "G#3": 207.65234878997256,
    "A3": 220.0,
    "A#3": 233.08188075904496,
    "B3": 246.94165062806206,
    "C4": 261.6255653005986,
    "C#4": 277.1826309768721,
    "D4": 293.6647679174076,
    "D#4": 311.1269837220809,
    "E4": 329.6275569128699,
    "F4": 349.2282314330039,
    "F#4": 369.9944227116344,
    "G4": 391.99543598174927,
    "G#4": 415.3046975799451,
    "A4": 440.0,
    "A#4": 466.1637615180899,
    "B4": 493.8833012561241,
    "C5": 523.2511306011972,
    "C#5": 554.3652619537442,
    "D5": 587.3295358348151,
    "D#5": 622.2539674441618,
    "E5": 659.2551138257398,
    "F5": 698.4564628660078,
    "F#5": 739.9888454232688,
    "G5": 783.9908719634985,
    "G#5": 830.6093951598903,
    "A5": 880.0,
    "A#5": 932.3275230361799,
    "B5": 987.7666025122483,
    "C6": 1046.5022612023945,
    "C#6": 1108.7305239074883,
    "D6": 1174.6590716696303,
    "D#6": 1244.5079348883237,
    "E6": 1318.5102276514797,
    "F6": 1396.9129257320155,
    "F#6": 1479.9776908465376,
    "G6": 1567.981743926997,
    "G#6": 1661.2187903197805,
    "A6": 1760.0,
    "A#6": 1864.6550460723597,
    "B6": 1975.5332050244965,
}

freq_list = [
    32.70319566257483,
    34.64782887210901,
    36.70809598967595,
    38.890872965260115,
    41.20344461410874,
    43.653528929125486,
    46.2493028389543,
    48.99942949771866,
    51.91308719749314,
    55.0,
    58.27047018976124,
    61.735412657015516,
    65.40639132514966,
    69.29565774421802,
    73.4161919793519,
    77.78174593052023,
    82.40688922821748,
    87.30705785825097,
    92.4986056779086,
    97.99885899543732,
    103.82617439498628,
    110.0,
    116.54094037952248,
    123.47082531403103,
    130.8127826502993,
    138.59131548843604,
    146.8323839587038,
    155.56349186104046,
    164.81377845643496,
    174.61411571650194,
    184.9972113558172,
    195.99771799087463,
    207.65234878997256,
    220.0,
    233.08188075904496,
    246.94165062806206,
    261.6255653005986,
    277.1826309768721,
    293.6647679174076,
    311.1269837220809,
    329.6275569128699,
    349.2282314330039,
    369.9944227116344,
    391.99543598174927,
    415.3046975799451,
    440.0,
    466.1637615180899,
    493.8833012561241,
    523.2511306011972,
    554.3652619537442,
    587.3295358348151,
    622.2539674441618,
    659.2551138257398,
    698.4564628660078,
    739.9888454232688,
    783.9908719634985,
    830.6093951598903,
    880.0,
    932.3275230361799,
    987.7666025122483,
    1046.5022612023945,
    1108.7305239074883,
    1174.6590716696303,
    1244.5079348883237,
    1318.5102276514797,
    1396.9129257320155,
    1479.9776908465376,
    1567.981743926997,
    1661.2187903197805,
    1760.0,
    1864.6550460723597,
    1975.5332050244965,
]

#!/usr/bin/python3
# notes adapted from:
# - https://h.bilibili.com/38456524?from=search&seid=5572416702001248050
# - https://www.qinyipu.com/jianpu/jianpudaquan/208503.html

encoding = "simple"
tracks = 2

raw = '''L6, T/0.25, L6, T/2, M6, T/4, M6, T/4, M7, T/4, M7, T/4, H1, T/4, H1, T/4, H2, T/4, H2, T/4, H1, T/4, H1, T/4, M7, T/4, M7, T/4, H1, T/4, H1, T/4,
L6, T/0.25, L6, T/2, M6, T/4, M6, T/4, M7, T/4, M7, T/4, H1, T/4, H1, T/4, H2, T/4, H2, T/4, H1, T/4, H1, T/4, H2, T/4, H2, T/4, H3, T/4, H3, T/4,
H4, T/2, H1, T/2, H4, T/2, H1, T/2, H5, T/2, H2, T/2, H5, T/2, H2, T/2,

S, T/2,

M6, T/2, M6, T/4, M6, T/4, M6, T/0.5, M6, T/4, M3, T/4, M6, T/4, M7, T/4,
H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/2, H2, T/2,
M5, T/0.5, M4, T, M3, T,
M2, T/0.33, S, T,

M6, T/2, M6, T/4, M6, T/4, M6, T/0.5, M6, T/4, M3, T/4, M6, T/4, M7, T/4,
H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/2, H2, T/2,
M5, T/0.5, S, T/4, M3, T/4, M4, T/4, M5, T/4,
M6, T/0.5, M7, T/0.5,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/4, M6, T/4, H1, T/4, H3, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, H4, T/2, H1, T/2,
H3, T/0.5, S, T/2, M5, T/2, M7, T/2, H1, T/2,
H2, T/0.5, H1, T, M7, T,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/4, M6, T/4, H1, T/4, H3, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, H5, T/2, H4, T/2,
H3, T, H1, T, S, T/2, M5, T/2, H1, T/2, H3, T/2,
H2, T/0.67, H2, T/4, H2, T/4, H3, T/2, H3, T/0.67,

S, T/2,

S, T/2, L6, T/2, M1, T/2, M3, T/2, M4, T, M1, T,
M3, T, M1, T, L7, T, L5, T,
S, T/2, L6, T/2, M1, T/2, M3, T/2, M6, T, M5, T/2, M4, T/2,
M3, T, M1, T, M2, T, L7, T,

S, T/2, L6, T/2, M1, T/2, M3, T/2, M4, T, M1, T,
M3, T, M1, T, L7, T, L6, T/2, L5, T/2,
M6, T/2, M7, T/2, H1, T, M6, T/2, M7, T/2, H1, T,
M7, T/4, H1, T/4, H2, T/0.66, H1, T, M7, T,

S, T/2, M3, T/2, M6, T/2, M7, T/2, M7, T, H1, T,
M5, T, M3, T, M4, T, M3, T/2, M2, T/2,
S, T/2, M3, T/2, M6, T/2, M7, T/2, M7, T, H1, T,
H3, T, H1, T, H2, T, H1, T/2, M7, T/2,

S, T/2, M3, T/2, M6, T/2, M7, T/2, H1, T, H3, T,
H5, T, H4, T/2, H3, T/2, H2, T, H1, T/2, M7, T/2,
M6, T/0.67, S, T/2, M6, T/4, M7, T/4, H1, T/0.67,
M7, T/4, H1, T/4, H2, T/0.67, H3, T/2, H3, T/0.67,

S, T/2,

M6, T/2, M6, T/4, M6, T/4, M6, T/0.5, M6, T/4, M3, T/4, M6, T/4, M7, T/4,
H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/2, H2, T/2,
M5, T/0.5, M4, T, M3, T,
M2, T/0.33, S, T,

M6, T/2, M6, T/4, M6, T/4, M6, T/0.5, M6, T/4, M3, T/4, M6, T/4, M7, T/4,
H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/2, H2, T/2,
M5, T/0.5, S, T/4, M3, T/4, M4, T/4, M5, T/4,
M6, T/0.5, M7, T/0.5,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/4, M6, T/4, H1, T/4, H3, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, H4, T/2, H1, T/2,
H3, T/0.5, S, T/2, M5, T/2, M7, T/2, H1, T/2,
H2, T/0.5, H1, T, M7, T,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H1, T/4, M6, T/4, H1, T/4, H3, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, H5, T/2, H4, T/2,
H3, T, H1, T, S, T/2, M5, T/2, H1, T/2, H3, T/2,
H2, T/0.67, H2, T/4, H2, T/4, H3, T/2, H3, T/0.67,

S, T/4, H6, T/4, H6, T/4, H6, T/4, S, T/2, S, T/4, H6, T/4, H6, T/4, H6, T/0.75,
'''

raw_c = '''L6, T/0.25, L6, T/2, M1, T/4, M1, T/4, M2, T/4, M2, T/4, M3, T/4, M3, T/4, M4, T/4, M4, T/4, M3, T/4, M3, T/4, M2, T/4, M2, T/4, M3, T/4, M3, T/4,
L6, T/0.25, L6, T/2, M1, T/4, M1, T/4, M2, T/4, M2, T/4, M3, T/4, M3, T/4, M4, T/4, M4, T/4, M3, T/4, M3, T/4, M4, T/4, M4, T/4, M5, T/4, M5, T/4,
M6, T/2, M4, T/2, M6, T/2, M4, T/2, M7, T/2, M5, T/2, M7, T/2, M5, T/2,

S, T/2,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H6, T/4, H3, T/4, H6, T/4, H7, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, U1, T/2, U2, T/2,
H1, T/0.5, H4, T, H3, T,
M5, T/0.33, S, T,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H6, T/4, H3, T/4, H6, T/4, H7, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, U1, T/2, U2, T/2,
H1, T/0.5, S, T/4, H3, T/4, H4, T/4, H5, T/4,
H2, T/0.5, H2, T/0.5,

H3, T/2, H3, T/4, H3, T/4, H3, T/0.5, U1, T/4, H6, T/4, U1, T/4, U3, T/4,
H6, T/2, H6, T/4, H6, T/4, H6, T/0.5, U4, T/2, U1, T/2,
H5, T/0.5, S, T/2, H5, T/2, H7, T/2, U1, T/2,
H5, T/0.5, U1, T, H7, T,

H3, T/2, H3, T/4, H3, T/4, H3, T/0.5, U1, T/4, H6, T/4, U1, T/4, U3, T/4,
H6, T/2, H6, T/4, H6, T/4, H6, T/0.5, U5, T/2, U4, T/2,
U3, T, U1, T, S, T/2, H5, T/2, U1, T/2, U3, T/2,
H5, T/0.67, U2, T/4, U2, T/4, H5, T/2, H5, T/0.67,

S, T/2,

S, T/2, L6, T/2, M1, T/2, M3, T/2, M4, T, M1, T,
M3, T, M1, T, L7, T, L5, T,
S, T/2, L6, T/2, M1, T/2, M3, T/2, M6, T, M5, T/2, M4, T/2,
M3, T, M1, T, M2, T, L7, T,

S, T/2, L6, T/2, M1, T/2, M3, T/2, M4, T, M1, T,
M3, T, M1, T, L7, T, L6, T/2, L5, T/2,
L6, T/2, L7, T/2, M1, T, L6, T/2, L7, T/2, M1, T,
L7, T/4, M1, T/4, M2, T/0.66, M1, T, L7, T,

S, T/2, M3, T/2, M6, T/2, M7, T/2, M7, T, H1, T,
M5, T, M3, T, M4, T, M3, T/2, M2, T/2,
S, T/2, M3, T/2, M6, T/2, M7, T/2, M7, T, H1, T,
H3, T, H1, T, H2, T, H1, T/2, M7, T/2,

S, T/2, M3, T/2, M6, T/2, M7, T/2, H1, T, H3, T,
H5, T, H4, T/2, H3, T/2, H2, T, H1, T/2, M7, T/2,
L6, T/0.67, S, T/2, L6, T/4, L7, T/4, M1, T/0.67,
L7, T/4, M1, T/4, M2, T/0.67, M3, T/2, M3, T/0.67,

S, T/2,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H6, T/4, H3, T/4, H6, T/4, H7, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, U1, T/2, U2, T/2,
H1, T/0.5, H4, T, H3, T,
M5, T/0.33, S, T,

H1, T/2, H1, T/4, H1, T/4, H1, T/0.5, H6, T/4, H3, T/4, H6, T/4, H7, T/4,
H4, T/2, H4, T/4, H4, T/4, H4, T/0.5, U1, T/2, U2, T/2,
H1, T/0.5, S, T/4, H3, T/4, H4, T/4, H5, T/4,
H2, T/0.5, H2, T/0.5,

H3, T/2, H3, T/4, H3, T/4, H3, T/0.5, U1, T/4, H6, T/4, U1, T/4, U3, T/4,
H6, T/2, H6, T/4, H6, T/4, H6, T/0.5, U4, T/2, U1, T/2,
H5, T/0.5, S, T/2, H5, T/2, H7, T/2, U1, T/2,
H5, T/0.5, U1, T, H7, T,

H3, T/2, H3, T/4, H3, T/4, H3, T/0.5, U1, T/4, H6, T/4, U1, T/4, U3, T/4,
H6, T/2, H6, T/4, H6, T/4, H6, T/0.5, U5, T/2, U4, T/2,
U3, T, U1, T, S, T/2, H5, T/2, U1, T/2, U3, T/2,
H5, T/0.67, U2, T/4, U2, T/4, H5, T/2, H5, T/0.67,

S, T/4, U6, T/4, U6, T/4, U6, T/4, S, T/2, S, T/4, U6, T/4, U6, T/4, U6, T/0.75,
'''

notes = [[57, 57, 69, 69, 71, 71, 72, 72, 74, 74, 72, 72, 71, 71, 72, 72], [57, 57, 69, 69, 71, 71, 72, 72, 74, 74, 72, 72, 74, 74, 76, 76], [77, 72, 77, 72, 79, 74, 79, 74], [], [20], [], [69, 69, 69, 69, 69, 64, 69, 71], [72, 72, 72, 72, 72, 74], [67, 65, 64], [62, 20], [], [69, 69, 69, 69, 69, 64, 69, 71], [72, 72, 72, 72, 72, 74], [67, 20, 64, 65, 67], [69, 71], [], [72, 72, 72, 72, 72, 69, 72, 76], [77, 77, 77, 77, 77, 72], [76, 20, 67, 71, 72], [74, 72, 71], [], [72, 72, 72, 72, 72, 69, 72, 76], [77, 77, 77, 77, 79, 77], [76, 72, 20, 67, 72, 76], [74, 74, 74, 76, 76], [], [20], [], [20, 57, 60, 64, 65, 60], [64, 60, 59, 55], [20, 57, 60, 64, 69, 67, 65], [64, 60, 62, 59], [], [20, 57, 60, 64, 65, 60], [64, 60, 59, 57, 55], [69, 71, 72, 69, 71, 72], [71, 72, 74, 72, 71], [], [20, 64, 69, 71, 71, 72], [67, 64, 65, 64, 62], [20, 64, 69, 71, 71, 72], [76, 72, 74, 72, 71], [], [20, 64, 69, 71, 72, 76], [79, 77, 76, 74, 72, 71], [69, 20, 69, 71, 72], [71, 72, 74, 76, 76], [], [20], [], [69, 69, 69, 69, 69, 64, 69, 71], [72, 72, 72, 72, 72, 74], [67, 65, 64], [62, 20], [], [69, 69, 69, 69, 69, 64, 69, 71], [72, 72, 72, 72, 72, 74], [67, 20, 64, 65, 67], [69, 71], [], [72, 72, 72, 72, 72, 69, 72, 76], [77, 77, 77, 77, 77, 72], [76, 20, 67, 71, 72], [74, 72, 71], [], [72, 72, 72, 72, 72, 69, 72, 76], [77, 77, 77, 77, 79, 77], [76, 72, 20, 67, 72, 76], [74, 74, 74, 76, 76], [], [20, 81, 81, 81, 20, 20, 81, 81, 81]]

notes_c = [[57, 57, 60, 60, 62, 62, 64, 64, 65, 65, 64, 64, 62, 62, 64, 64], [57, 57, 60, 60, 62, 62, 64, 64, 65, 65, 64, 64, 65, 65, 67, 67], [69, 65, 69, 65, 71, 67, 71, 67], [], [20], [], [72, 72, 72, 72, 81, 76, 81, 83], [77, 77, 77, 77, 72, 74], [72, 77, 76], [67, 20], [], [72, 72, 72, 72, 81, 76, 81, 83], [77, 77, 77, 77, 72, 74], [72, 20, 76, 77, 79], [74, 74], [], [76, 76, 76, 76, 72, 81, 72, 76], [81, 81, 81, 81, 77, 72], [79, 20, 79, 83, 72], [79, 72, 83], [], [76, 76, 76, 76, 72, 81, 72, 76], [81, 81, 81, 81, 79, 77], [76, 72, 20, 79, 72, 76], [79, 74, 74, 79, 79], [], [20], [], [20, 57, 60, 64, 65, 60], [64, 60, 59, 55], [20, 57, 60, 64, 69, 67, 65], [64, 60, 62, 59], [], [20, 57, 60, 64, 65, 60], [64, 60, 59, 57, 55], [57, 59, 60, 57, 59, 60], [59, 60, 62, 60, 59], [], [20, 64, 69, 71, 71, 72], [67, 64, 65, 64, 62], [20, 64, 69, 71, 71, 72], [76, 72, 74, 72, 71], [], [20, 64, 69, 71, 72, 76], [79, 77, 76, 74, 72, 71], [57, 20, 57, 59, 60], [59, 60, 62, 64, 64], [], [20], [], [72, 72, 72, 72, 81, 76, 81, 83], [77, 77, 77, 77, 72, 74], [72, 77, 76], [67, 20], [], [72, 72, 72, 72, 81, 76, 81, 83], [77, 77, 77, 77, 72, 74], [72, 20, 76, 77, 79], [74, 74], [], [76, 76, 76, 76, 72, 81, 72, 76], [81, 81, 81, 81, 77, 72], [79, 20, 79, 83, 72], [79, 72, 83], [], [76, 76, 76, 76, 72, 81, 72, 76], [81, 81, 81, 81, 79, 77], [76, 72, 20, 79, 72, 76], [79, 74, 74, 79, 79], [], [20, 81, 81, 81, 20, 20, 81, 81, 81]]

tempo = [[2000, 250, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125], [2000, 250, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125, 125], [250, 250, 250, 250, 250, 250, 250, 250], [], [250], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 500, 500], [1515, 500], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 125, 125, 125, 125], [1000, 1000], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 250, 250, 250, 250], [1000, 500, 500], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [500, 500, 250, 250, 250, 250], [746, 125, 125, 250, 746], [], [250], [], [250, 250, 250, 250, 500, 500], [500, 500, 500, 500], [250, 250, 250, 250, 500, 250, 250], [500, 500, 500, 500], [], [250, 250, 250, 250, 500, 500], [500, 500, 500, 250, 250], [250, 250, 500, 250, 250, 500], [125, 125, 757, 500, 500], [], [250, 250, 250, 250, 500, 500], [500, 500, 500, 250, 250], [250, 250, 250, 250, 500, 500], [500, 500, 500, 250, 250], [], [250, 250, 250, 250, 500, 500], [500, 250, 250, 500, 250, 250], [746, 250, 125, 125, 746], [125, 125, 746, 250, 746], [], [250], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 500, 500], [1515, 500], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 125, 125, 125, 125], [1000, 1000], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [1000, 250, 250, 250, 250], [1000, 500, 500], [], [250, 125, 125, 1000, 125, 125, 125, 125], [250, 125, 125, 1000, 250, 250], [500, 500, 250, 250, 250, 250], [746, 125, 125, 250, 746], [], [125, 125, 125, 125, 250, 125, 125, 125, 666]]

# convert raw to compatible MIDI notes format
if __name__=="__main__":
    notes = []
    tempo = []

    L0 = 48  # C3
    M0 = 60  # C4
    H0 = 72  # C5
    U0 = 84  # C6

    offset = [0, 0, 2, 4, 5, 7, 9, 11, 12]
    tempo_base = 500

    b = raw

    notes_t = []
    tempo_t = []

    exit = False

    while not exit:
        if b.find(',') != -1:
            a, b = ( b.split(',', 1) )
        else:
            a = b
            exit = True

        a = a.strip(' ')

        print(a)

        if a[0] == "L":
            note = L0 + offset[int(a[1])]
            notes_t.append(note)
        elif a[0] == "M":
            note = M0 + offset[int(a[1])]
            notes_t.append(note)
        elif a[0] == "H":
            note = H0 + offset[int(a[1])]
            notes_t.append(note)
        elif a[0] == "U":
            note = H0 + offset[int(a[1])]
            notes_t.append(note)
        elif a[0] == "S":
            note = 20
            notes_t.append(note)
        elif a[0] == "T":
            if a == "T":
                t = tempo_base
            else:
                _,div = a.split('/')
                t = int( tempo_base / float(div) )
            tempo_t.append(t)
        elif a[0] == "\n" or a[0] == "\r":
            notes.append(notes_t)
            tempo.append(tempo_t)
            notes_t = []
            tempo_t = []

            b = a[1:] + ', ' + b
        else:
            pass

        # print(tempo_t)
        # print(notes_t)

    print("notes =", end=' ')
    print(notes)
    print("tempo =", end=' ')
    print(tempo)
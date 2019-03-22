# task5 **
# Перед вами https://gist.github.com/deliro/aaa2a44b1fe283c98ca50823c3ebd335 странный словарь.
# В нём зашифровано послание. Ключи словаря — ASCII символы.
# Но не просто символы, в них инвертированы последние два младших бита.
# Значения — список позиций в строке, где этот символ (ключ) встречается.
# Расставьте символы в правильные позиции и вы расшифруете послание.

susp_dct = {9: [0, 77, 154, 231, 308, 385, 462],
            35: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 82, 83, 84, 89,
                 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,
                 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 131, 132, 133, 134, 135, 136, 137, 138, 139,
                 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 155, 157, 158, 162, 163, 170,
                 180, 181, 190, 196, 197, 198, 199, 200, 201, 205, 206, 208, 214, 222, 223, 229, 230, 232, 233, 236,
                 237, 238, 239, 242, 246, 249, 250, 253, 254, 259, 261, 262, 268, 272, 274, 275, 276, 277, 279, 283,
                 286, 290, 293, 294, 295, 296, 297, 298, 301, 305, 307, 309, 310, 311, 312, 314, 315, 317, 319, 323,
                 326, 327, 330, 331, 333, 334, 335, 336, 338, 339, 341, 342, 343, 345, 346, 347, 351, 352, 353, 354,
                 356, 360, 363, 367, 370, 371, 374, 375, 378, 379, 380, 384, 386, 387, 388, 389, 394, 395, 401, 402,
                 409, 410, 411, 412, 413, 418, 419, 420, 421, 428, 429, 430, 431, 432, 438, 439, 445, 454, 461, 463,
                 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483,
                 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503,
                 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523,
                 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538],
            47: [78, 85, 102, 127, 165, 171, 175, 183, 191, 202, 209, 215, 218, 221, 224],
            46: [79, 80, 86, 87, 103, 104, 128, 129, 166, 167, 168, 172, 173, 176, 177, 184, 185, 187, 188, 192, 193,
                 194, 203, 210, 211, 212, 216, 217, 219, 220, 225, 226, 227, 244, 257, 264, 265, 270, 281, 288, 303,
                 321, 348, 349, 358, 365, 381, 382, 391, 392, 397, 398, 399, 404, 405, 406, 407, 415, 416, 423, 424,
                 425, 426, 434, 435, 436, 441, 442, 443, 447, 448, 451, 452, 456, 457, 458, 459],
            45: [81, 88, 105, 130, 160, 169, 174, 178, 186, 189, 195, 213, 228, 235, 243, 245, 263, 269, 271, 280, 282,
                 287, 289, 302, 304, 350, 383], 95: [156, 299, 344, 355, 377],
            99: [159, 256, 357, 390, 396, 403, 414, 422, 433, 440, 446, 455],
            36: [161, 234, 258, 266, 278, 318, 320, 322, 324, 325, 328, 329, 332, 359, 362, 364, 366, 368, 393, 400,
                 408, 417, 427, 437, 444, 449, 450, 453, 460],
            44: [164, 240],
            127: [179, 182, 204, 207, 241, 247, 248, 251, 252, 255, 260, 267, 284, 285, 291, 292, 300, 313, 316, 337,
                  340, 361, 369, 372, 373, 376],
            57: [273, 306]}

if isinstance(susp_dct, dict):

    inv_d = {}

    for k in susp_dct:
        for i in susp_dct[k]:
            try:
                inv_d[i] = k ^ 0b00000011
            except TypeError:
                print('Ошибка типа данных. Ожидается int в ключах')
                exit()
    try:
        print(''.join([chr(inv_d[k]) for k in sorted(inv_d)]))
    except TypeError:
        print('Ошибка типа данных. Ожидается int в значениях словаря')

else:
    print('Ошибка ввода. Ожидается dict')


# Результат:
# $ python3 task5.py
#
# ,--.   ,--.             ,--.                     ,--.
#  \  `.'  /,---. ,--.,--.|  |,--.--. ,---.      ,-|  | ,---. ,--,--,  ,---.
#   '.    /| .-. ||  ||  |`-' |  .--'| .-. :    ' .-. || .-. ||      \| .-. :
#     |  | ' '-' ''  ''  '    |  |   \   --.    \ `-' |' '-' '|  ||  |\   --.
#     `--'  `---'  `----'     `--'    `----'     `---'  `---' `--''--' `----'
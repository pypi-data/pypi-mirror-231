
# playfair_cipher.py by  @Shailesh and Siddhesh
def matrix(key):
    atoz = list('abcdefghiklmnopqrstuvwxyz')
    matrix = [[] for i in range(5)]  
    r = 0  # row
    c = 0  # column
    key = key.lower()  # Convert the key to lowercase
    for i in key:
        if i in atoz:
            matrix[r].append(i)
            atoz.remove(i)
            c += 1
            if c > 4:
                r += 1
                c = 0

    for i in atoz:
        matrix[r].append(i)
        c += 1
        if c > 4:
            r += 1
            c = 0
    return matrix

def pairs(plainText):
    plainText = plainText.lower()  # Convert the plaintext to lowercase
    plainText = plainText.replace(" ", "")
    for s in range(0, len(plainText) + 1, 2):
        if s < len(plainText) - 1:
            if plainText[s] == plainText[s + 1]:
                plainText = plainText[:s + 1] + 'x' + plainText[s + 1:]

    if len(plainText) % 2 != 0:
        plainText = plainText[:] + 'x'

    pair_list = [plainText[i:i + 2] for i in range(0, len(plainText), 2)]
    return pair_list

def encryption(pt_pairs, matrix):
    ciphertext_pairs = []
    for pair in pt_pairs:
        applied_rule = False
        for row in matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.index(pair[0])
                j1 = row.index(pair[1])
                ct_pair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                ciphertext_pairs.append(ct_pair)
                applied_rule = True

        if applied_rule:
            continue

        for j in range(5):
            col = [matrix[i][j] for i in range(5)]

            if pair[0] in col and pair[1] in col:
                i0 = col.index(pair[0])
                i1 = col.index(pair[1])
                ct_pair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                ciphertext_pairs.append(ct_pair)
                applied_rule = True

        if applied_rule:
            continue

        i0 = i1 = j0 = j1 = 0
        for i in range(5):
            row = matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.index(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.index(pair[1])

        ct_pair = matrix[i0][j1] + matrix[i1][j0]
        ciphertext_pairs.append(ct_pair)
    return "".join(ciphertext_pairs)


def decryption(ciphertext, matrix):
    ciphertext = ciphertext.lower()  # Convert the ciphertext to lowercase
    ciphertext = ciphertext.replace(" ", "")
    ct_pairs = [ciphertext[i:i + 2] for i in range(0, len(ciphertext), 2)]

    plaintext = []
    for pair in ct_pairs:
        applied_rule = False
        for row in matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.index(pair[0])
                j1 = row.index(pair[1])
                pt_pair = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                plaintext.append(pt_pair)
                applied_rule = True

        if applied_rule:
            continue

        for j in range(5):
            col = [matrix[i][j] for i in range(5)]

            if pair[0] in col and pair[1] in col:
                i0 = col.index(pair[0])
                i1 = col.index(pair[1])
                pt_pair = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                plaintext.append(pt_pair)
                applied_rule = True

        if applied_rule:
            continue

        i0 = i1 = j0 = j1 = 0
        for i in range(5):
            row = matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.index(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.index(pair[1])

        pt_pair = matrix[i0][j1] + matrix[i1][j0]
        plaintext.append(pt_pair)

    return "".join(plaintext)

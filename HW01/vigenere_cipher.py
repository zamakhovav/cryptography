__author__ = 'Veronika Zamakhova'
import string


def decrypter(ciphertext, key):
    """
    Simple decrypter for a vigenere cipher given a key.
    :param ciphertext: The encrypted message.
    :param key: The key.
    :return: Returns the plaintext message.
    """
    message = ""
    current_place = 0
    for x in range(len(ciphertext)):
        c = ciphertext[x]
        k = key[current_place]
        current_place = (current_place + 1) % len(key)
        message += chr((ord(c) - ord(k)) % 26 + 65)
    return message


def numbers_to_letters(numbers_list):
    """
    Converts a list of numbers to uppercase letters
    :param numbers_list: List of numbers
    :return: Letters.
    """
    letters = ""
    for num in numbers_list:
        letters += chr(64 + num)
    print(letters)  # SALT
    return letters


def get_max_freq(percent_list):
    """
    Function that creates a list with all of the frequency possibilities to find the greatest overlap between
    the frequency of English and the frequency of the cipher text
    :param percent_list: The frequency of the letters
    :return: A list with all the frequency possibilities
    """

    english_freq = {'A': 8.17, 'B': 1.29, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97,
             'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93, 'Q': 0.10, 'R': 5.99,
             'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97, 'Z': 0.07}

    ordered_freq = []
    for letter in string.ascii_uppercase:
        ordered_freq.append(english_freq[letter])
    # print(ordered_freq)  # [8.17, 1.29, 2.78, 4.25, 12.7, 2.23, ... ]

    temp_percent = percent_list[:]
    combination_list = []
    for x in range(26):
        temp_total = 0
        for y in range(26):
            temp_total += ordered_freq[y] * temp_percent[y]
        combination_list.append(temp_total)
        temp_percent = shift(temp_percent, 1)
    return combination_list.index(max(combination_list))  # 18 0 11 19


def shift(someList, n):
    """
    Simple shift method to emulate a circular
    :param someList:
    :param n:
    :return:
    """
    return someList[n:] + someList[:n]


def percentage_maker(ciphertext, key_len, key_shift):
    """
    Takes in the encrypted message and the key length and creates a frequency percentage
    :param ciphertext: The encrypted message.
    :param key_len: The length of the key.
    :return: A list of percents for how often a letter occurs
    """
    freq_dict = {letter: 0 for letter in string.ascii_uppercase}  # {'A': 0, 'B': 0, 'C': 0,
    for x in range(len(ciphertext)):
        if x % key_len == key_shift:
            freq_dict[ciphertext[x]] += 1
    # freq_dict: {'A': 21, 'B': 0, 'C': 1, 'D': 15,

    percent_list = []
    for letter in string.ascii_uppercase:
        percent_list.append(freq_dict[letter] / len(ciphertext))
    # print("PERCENT_LIST:", percent_list)  # PERCENT_LIST: [0.01784197111299915, 0.0, 0.0008496176720475786, .. ]
    return percent_list


def coincidence_finder(ciphertext, matrix):
    """
    Calculates the number of coincidences per possible string
    :param ciphertext: The encrypted message
    :param matrix: The grid of shifted messages
    :return: The list of coincidences in order, used to determine the key length.
    ===============
    THE RESULT:
    ZIP lists: [('G', 36), ('T', 46), ('Y', 52), ('S', 82), ('M', 42), ('D', 48), ... ]
    ===============
    """
    coincidence_list = []
    letter_list = []
    for offset in matrix:
        counter = 0
        for x in range(len(ciphertext)):
            if offset[x] == ciphertext[x]:
                counter += 1
        letter_list.append(offset[x])
        coincidence_list.append(counter)
    print("Zip lists:", list(zip(letter_list, coincidence_list)))
    return coincidence_list


def grid_printer(matrix):
    """
    pretty prints the matrix grid
    :param matrix: The encrypted message grid
    :return: None
    """
    for x in matrix:
        print(x)


def grid_generator(ciphertext):
    """
    Generates the 'grid' of offset encrypted text
    :param ciphertext: The encrypted message
    :return: returns a matrix that is primed for the coincidences counter
    ================
    THE RESULT:
    LHPLWSTMMAEB… – origin cipher text for comparing
     LHPLWSTMMAE… – coincidence is 1
      LHPLWSTMMA… - coincidence is 0
       LHPLWSTMM… - coincidence is 1
        LHPLWSTM…
         LHPLWST…
          LHPLWS…
           LHPLW…
            LHPL…
             LHP…
              LH…
               L…
    =================

    """
    matrix = []
    for x in range(1, len(ciphertext)):
        temporary_string = "-" * x
        temporary_string += ciphertext[:len(ciphertext) - x]
        matrix.append(temporary_string)
    return matrix


def main():
    CIPHERTEXT = "LHPLWSTMMAEBGNDTKRPVSLWXVBJIDAEHSNOTKVTOADWRSCEXVUAHFBJVGREXRHLOWANHEMZGSNOBFTPKWSEBFGFGVECEQIY" \
                "ZDORBUNZMACPMZAEMZEDHDDTXJSLKWNZMEOEBNAEXVTZKWTCXSTUNKTZKWVPGEATGDYMRLHPBJRLMAOYTDADLWSDFWNEHX" \
                "TSXVAYZWRDHXBLMLLPTFDMRLHPBJSPEXIYMWRPLLRLMZECMZEJWASNHNECTKOFGVRPTKOYMGRFGSWLRTYCXSLTSANRMZAEP" \
                "ZAEBLMLDWSDXFSPYGREAWMEHVOOXHEYWKOYPZAEBLWTEDMLDWSPGKEQHJOEAWRDMGDZTFDEASTLEDOQMZEZMZECLUAYGGTT" \
                "VWTSBKTZHWVPGSQFBLEMKSVPLGLOBWRXTQPCXXECMGRFGJAEAWREASNSXJOTVSLWRTUEIGIYMDEDLDYOBWTCRANRMGSEXET" \
                "SXGNNHEIYZLIOXSLWUQHTFKEWYLHFLOENHMLOBEARBFEHBLHZNLCZGLRLWACEBGNLVARNNESETFCPBFWSBUHLGSRXRSLWHXW" \
                "SHKEXXEBPKKACXTRLOWFWXWSLMLOALHEPWTEQHJEEAWEYXEYXTCEDTEOGXAFEAWSZEVIPKKRPTDLJTJEMKSVPMZEYMZIDLMR" \
                "PEQIDGLTSXGUEVGMPTFYZYLHPFOAYMWDPTUHHHMLOASVPIJEQXJRPWLHLMSLWLLAYWSNOYAGSMOHLMOESTNESXJEEAWNTLSCLL" \
                "WIYPZINALHPBFTPKSCEBGNZYEAYRANOBNIONSLWRJAEBGNLEVENBKIZGEAVBFGAKGCPLKEDHFEAKGCPLKPPKKOWWAECIJOON" \
                "UEDTFOFMUOXXANEXFDPWTYYHGNPFGSETJMTXKTCRLOLOGIOMZIDIJOMEWMUNKTLLUOCMWZOBVSTGUEEAWYNTFTFLMAWEQMLD" \
                "WRPMJELMHHJLACLEDYTFHODLABWXLHPREAVXATPVGNZFACLEDYTFHODLABWXLHPRKHZHLDPLWREXJSEAWNDMSNOBFGLGVFTZ" \
                "ZTTGYIDXSCSLGLOBWRDBFDTOADFTDLJKSTTHFAWVGUCLWOQTUTTHFAQMWRLEDBPVSUDXLHPVGSEHXRFGFIYZASDNJEEHTELMD" \
                "ELLLADAAGSTKTSXUODMGFDMSYTGY"

    matrix = grid_generator(CIPHERTEXT)
    # grid_printer(matrix)

    coincidence_list = coincidence_finder(CIPHERTEXT, matrix)
    temporary_list = coincidence_list[:10]
    print("TEM", temporary_list)  # TEM [36, 46, 52, 82, 42, 48, 45, 75, 46, 44]
    temporary_key = temporary_list.index(max(temporary_list)) + 1
    print("Length of key", temporary_key)  # 4

    key_len = temporary_key
    key = []
    for x in range(key_len):
        percent_list = percentage_maker(CIPHERTEXT, key_len, x)
        combination_list = get_max_freq(percent_list) + 1
        key.append(combination_list)
    new_key = numbers_to_letters(key)
    message = decrypter(CIPHERTEXT, new_key)

    print("=" * 19, "CIPHERTEXT", "=" * 19)
    print(CIPHERTEXT)
    print("=" * 50)
    print("KEY:", new_key)
    print("=" * 50)
    print("=" * 19, "PLAINTEXT", "=" * 19)
    print(message)
    print("=" * 50)


if __name__ == "__main__":
    main()


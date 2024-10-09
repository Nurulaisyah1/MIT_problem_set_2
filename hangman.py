# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Memuat daftar kata dari file...")
    inFile = open(WORDLIST_FILENAME, 'r')  # Membuka file untuk dibaca
    line = inFile.readline()  # Membaca satu baris dari file
    wordlist = line.split()  # Memecah baris menjadi daftar kata
    print("  ", len(wordlist), "kata dimuat.")
    return wordlist




def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)  # Memilih kata secara acak

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program

# Memuat daftar kata ke dalam variabel wordlist
wordlist = load_words()


## helper functions

# fungsi ini memeriksa apakah semua huruf dari kata rahasia (secret_word) sudah ditebak.
def is_word_guessed(secret_word, letters_guessed):
    '''
    Returns True if all letters in the secret_word are in letters_guessed.
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False  # Jika ada huruf yang belum ditebak, kembalikan False
    return True  # Semua huruf sudah ditebak

#Fungsi ini mengembalikan kata yang telah ditebak sejauh ini, dengan tanda _ untuk huruf yang belum ditebak.
def get_guessed_word(secret_word, letters_guessed):
    '''
    Returns a string representing the guessed word so far.
    '''
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter  # Tambahkan huruf yang sudah ditebak
        else:
            guessed_word += '_ '  # Tambahkan _ untuk huruf yang belum ditebak
    return guessed_word


#Fungsi ini mengembalikan huruf-huruf yang belum ditebak.
def get_available_letters(letters_guessed):
    '''
    Returns a string of available letters that have not been guessed yet.
    '''
    all_letters = string.ascii_lowercase  # Mengambil semua huruf kecil
    available_letters = ''
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter  # Tambahkan huruf yang belum ditebak
    return available_letters

    
    
#Fungsi utama yang menjalankan permainan Hangman. Pemain memulai dengan 6 tebakan, dan setiap huruf yang salah mengurangi jumlah tebakan.
def hangman(secret_word):
    '''
    Main game function for Hangman.
    '''
    guesses_left = 6  # Jumlah tebakan yang tersisa
    letters_guessed = []  # Daftar huruf yang telah ditebak

    print("Selamat datang di permainan Hangman!")
    print(f"Saya sedang memikirkan sebuah kata yang terdiri dari {len(secret_word)} huruf.")

    while guesses_left > 0:  # Selama tebakan masih ada
        print("------------")
        print(f"Kamu memiliki {guesses_left} tebakan tersisa.")
        print(f"Huruf yang tersedia: {get_available_letters(letters_guessed)}")
        guess = input("Silakan tebak sebuah huruf: ").lower()  # Menerima input tebakan

        if guess in letters_guessed:  # Jika huruf sudah ditebak
            print("Oops! Kamu sudah menebak huruf itu:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:  # Jika tebakan benar
            letters_guessed.append(guess)  # Tambahkan huruf yang ditebak ke daftar
            print("Tebakan yang baik:", get_guessed_word(secret_word, letters_guessed))
        else:  # Jika tebakan salah
            letters_guessed.append(guess)  # Tambahkan huruf yang ditebak ke daftar
            guesses_left -= 1  # Kurangi jumlah tebakan yang tersisa
            print("Oops! Huruf itu tidak ada dalam kata saya:", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):  # Jika kata sudah ditebak
            print("------------")
            print("Selamat, kamu menang!")
            break
    else:
        print("------------")
        print(f"Maaf, kamu kehabisan tebakan. Kata itu adalah {secret_word}.")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


#Fungsi ini memeriksa apakah kata lain (other_word) cocok dengan tebakan saat ini (my_word), di mana karakter _ adalah huruf yang belum ditebak.
# Fungsi untuk mencocokkan kata
def match_with_gaps(my_word, other_word):
    '''
    Returns True if the letters in my_word match other_word, with _ representing
    letters that haven't been guessed yet.
    '''
    my_word = my_word.replace(' ', '')  # Hilangkan spasi dari my_word
    if len(my_word) != len(other_word):  # Memeriksa panjang kata
        return False

    for my_letter, other_letter in zip(my_word, other_word):
        if my_letter != '_' and my_letter != other_letter:  # Memeriksa setiap huruf
            return False
    return True

#Fungsi ini menampilkan semua kata yang sesuai dengan tebakan sementara (my_word), di mana karakter _ belum ditebak.
def show_possible_matches(my_word):
    '''
    Prints out all words in the wordlist that match my_word with _ characters.
    '''
    possible_matches = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)  # Menambahkan kata yang cocok

    if possible_matches:
        print("Kata kemungkinan yang cocok adalah:", ' '.join(possible_matches))
    else:
        print("Tidak ada yang cocok")



#Fungsi ini adalah versi permainan Hangman yang dilengkapi dengan fitur hint. Jika pengguna menebak simbol *, maka daftar kemungkinan kata yang sesuai dengan tebakan saat ini akan ditampilkan.
def hangman_with_hints(secret_word):
    '''
    Main game function for Hangman with hints.
    '''
    guesses_left = 6
    letters_guessed = []

    print("Selamat datang di permainan Hangman!")
    print(f"Saya sedang memikirkan sebuah kata yang terdiri dari {len(secret_word)} huruf.")
    print("Kamu dapat meminta petunjuk dengan menebak '*'.")
    
    while guesses_left > 0:
        print("------------")
        print(f"Kamu memiliki {guesses_left} tebakan tersisa.")
        print(f"Huruf yang tersedia: {get_available_letters(letters_guessed)}")
        guess = input("Silakan tebak sebuah huruf: ").lower()

        if guess == "*":  # Jika pengguna meminta petunjuk
            print("Kemungkinan kata yang cocok:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        elif guess in letters_guessed:  # Jika huruf sudah ditebak
            print("Oops! Kamu sudah menebak huruf itu:", get_guessed_word(secret_word, letters_guessed))
        elif guess in secret_word:  # Jika tebakan benar
            letters_guessed.append(guess)
            print("Tebakan yang baik:", get_guessed_word(secret_word, letters_guessed))
        else:  # Jika tebakan salah
            letters_guessed.append(guess)
            guesses_left -= 1
            print("Oops! Huruf itu tidak ada dalam kata saya:", get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed):  # Jika kata sudah ditebak
            print("------------")
            print("Selamat, kamu menang!")
            break
    else:
        print("------------")
        print(f"Maaf, kamu kehabisan tebakan. Kata itu adalah {secret_word}.")


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
# Untuk memainkan permainan tanpa hints
   # osecret_word = choose_word(wordlist)
   # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    #untuk memainkan dengan bantuan
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

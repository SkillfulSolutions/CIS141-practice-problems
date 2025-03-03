'''
#1. Create a file called gardening_tips.txt and add at least 3 gardening tips to it.
    Write a Python script that reads a file gardening_tips.txt and prints
    out each tip one by one.
'''
with open('gardening_tips.txt', 'w') as f:
    f.write('1. Use vermicompost and fish compost.\n')
    f.write('2. Use only organic amendments.\n')
    f.write('3. Use an automatic watering system.\n')

with open("gardening_tips.txt","r") as f:
    line_count = 0
    for line in f:
        line_count += 1
        if line_count == 1:
            print(line.strip())
        if line_count == 2:
            print(line.strip())
        if line_count == 3:
            print(line.strip())
            break

'''
#2. Write a Python program that allows users to log their hiking trips. The program should:
    Open a file in append mode
    Use a while loop to repeatedly ask for a (hike name) and (distance) in miles
    Save each entry to hiking_log.txt (each hike on a new line)
    When the user presses 0, exit the loop & print the contents of hiking_log.txt
    Close the file
'''
file = open("hiking_log.txt","w")
while True:
    hike_name = input("What is the name of the hike you wish to log? Press 0 to exit. ")
    if hike_name == "0":
        break
    distance = input("What is the distance of the hike, in miles? Press 0 to exit. ")
    if distance == "0":
        break
    print()
    log_entry = hike_name + '\t' + distance + '\n'
    file.write(log_entry)
file.close()

'''
#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into it. Write a Python program that:
    - Reads the file
    - Requests 5 inputs from the user: 5 words the user would like to count the frequency of
    - Counts how many times each word appears
    - Creates a dictionary of the words and their counts
    - Print the dictionary to the console
'''
with open('song_lyrics.txt', 'w') as f:
    f.write("Are you going to Scarborough Fair: Parsley, sage, rosemary and thyme. Remember me to one who lives there. She once was a true love of mine. On the side of a hill in the deep forest green. Tracing of sparrow on snow-crested brown. Blankets and bedclothes the child of the mountain. Sleeps unaware of the clarion call. Tell her to make me a cambric shirt: Parsley, sage, rosemary and thyme; Without no seams nor needle work, Then she'll be a true love of mine. On the side of a hill in the sprinkling of leaves. Washes the grave with silvery tears. A soldier cleans and polishes a gun. Sleeps unaware of the clarion call. Tell her to find me an acre of land: Parsley, sage, rosemary and thyme; Between the salt water and the sea strands, Then she'll be a true love of mine. War bellows blazing in scarlet battalions. Generals order their soldiers to kill. And to fight for a cause they have long ago forgotten. Tell her to reap it with a sickle of leather: Parsley, sage, rosemary and thyme; And gather it all in a bunch of heather, Then she'll be a true love of mine. Are you going to Scarborough Fair: Parsley, sage, rosemary and thyme. Remember me to one who lives there. She once was a true love of mine.")

with open('song_lyrics.txt', 'r') as f:
    song = f.read()
    lyrics = song.lower()
    entry = input("Enter five words that you would like to count the frequency of separated by a single space. ")
    words = entry.lower()
    sep_words = words.split()
    word_counts = {}
    for i in sep_words:
        word_counts[i] = lyrics.count(i)
    print(word_counts)

'''
#4. Create a poll.txt file that contains a list of "yea" or "nay" votes separated by commas.
    Write a program that reads the poll.txt file
    Count how many votes "yea" or "nay" received and print the results.
'''
while True:
    with open('poll.txt', 'a') as f:
        vote_prompt = input("Is your vote 'yea' or 'nay'? Enter '0' to see results without voting. ")
        if vote_prompt == "0":
            break
        elif vote_prompt.lower() == "yea":
            f.write(vote_prompt.lower() + ", ")
        elif vote_prompt.lower() == "nay":
            f.write(vote_prompt.lower() + ", ")
        else:
            print("Please enter a valid vote. Also, no abstentions.")

with open('poll.txt', 'r') as f:
    votes = (f.readline()).split(", ")
    print(votes.count("yea"), "yeas")
    print(votes.count("nay"), "nays")

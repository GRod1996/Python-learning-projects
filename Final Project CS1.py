# Create the dictionary
music_database = {
    "rock": [
        "Bohemian Rhapsody - Queen",
        "Hotel California - Eagles",
        "Stairway to Heaven - Led Zeppelin",
        "Back in Black - AC/DC",
        "Smoke on the Water - Deep Purple",
        "Sweet Child O' Mine - Guns N' Roses",
        "Living on a Prayer - Bon Jovi",
        "Highway to Hell - AC/DC",
        "Paradise City - Guns N' Roses",
        "Rocket Man - Elton John",
        "Tiny Dancer - Elton John",
        "Your Song - Elton John",
        "Bennie and the Jets - Elton John",
        "Candle in the Wind - Elton John",
        "Born to Run - Bruce Springsteen",
        "Dream On - Aerosmith",
        "Free Fallin' - Tom Petty",
    ],
    "pop": [
        "Blinding Lights - The Weeknd",
        "Shape of You - Ed Sheeran",
        "Levitating - Dua Lipa",
        "Bad Guy - Billie Eilish",
        "Uptown Funk - Mark Ronson ft. Bruno Mars",
        "As It Was - Harry Styles",
        "Watermelon Sugar - Harry Styles",
        "Roar - Katy Perry",
        "Sorry - Justin Bieber",
        "Shake It Off - Taylor Swift",
        "Firework - Katy Perry",
        "Can't Stop the Feeling! - Justin Timberlake",
    ],
    "jazz": [
        "Take Five - Dave Brubeck",
        "So What - Miles Davis",
        "Feeling Good - Nina Simone",
        "My Favorite Things - John Coltrane",
        "Fly Me to the Moon - Frank Sinatra",
        "Blue in Green - Bill Evans",
        "Autumn Leaves - Cannonball Adderley",
        "All Blues - Miles Davis",
        "In a Sentimental Mood - Duke Ellington & John Coltrane",
        "Round Midnight - Thelonious Monk",
        "A Night in Tunisia - Dizzy Gillespie",
    ],
    "classical": [
        "Clair de Lune - Debussy",
        "Symphony No. 5 - Beethoven",
        "The Four Seasons - Vivaldi",
        "Canon in D - Pachelbel",
        "Swan Lake - Tchaikovsky",
        "Moonlight Sonata - Beethoven",
        "Eine kleine Nachtmusik - Mozart",
        "Ride of the Valkyries - Wagner",
        "Ave Maria - Schubert",
        "Piano Concerto No. 2 - Rachmaninoff",
        "Boléro - Ravel",
    ],
    "hip hop": [
        "Lose Yourself - Eminem",
        "Sicko Mode - Travis Scott",
        "God's Plan - Drake",
        "Alright - Kendrick Lamar",
        "Juicy - The Notorious B.I.G.",
        "Empire State of Mind - Jay-Z & Alicia Keys",
        "Stronger - Kanye West",
        "HUMBLE. - Kendrick Lamar",
        "Hotline Bling - Drake",
        "N.Y. State of Mind - Nas",
        "Gold Digger - Kanye West",
    ],
    "electronic": [
        "Strobe - Deadmau5",
        "One More Time - Daft Punk",
        "Levels - Avicii",
        "Lean On - Major Lazer",
        "Shelter - Porter Robinson & Madeon",
        "Animals - Martin Garrix",
        "Titanium - David Guetta ft. Sia",
        "Wake Me Up - Avicii",
        "Faded - Alan Walker",
        "Scary Monsters and Nice Sprites - Skrillex",
        "Ghosts 'n' Stuff - Deadmau5",
    ],
    "reggae": [
        "No Woman, No Cry - Bob Marley",
        "Three Little Birds - Bob Marley",
        "Bad Boys - Inner Circle",
        "Sweat (A La La La La Long) - Inner Circle",
        "Bam Bam - Sister Nancy",
        "Is This Love - Bob Marley",
        "Buffalo Soldier - Bob Marley",
    ],
    "country": [
        "Take Me Home, Country Roads - John Denver",
        "Jolene - Dolly Parton",
        "Friends in Low Places - Garth Brooks",
        "Tennessee Whiskey - Chris Stapleton",
        "The Gambler - Kenny Rogers",
        "Ring of Fire - Johnny Cash",
        "Before He Cheats - Carrie Underwood",
        "Need You Now - Lady A",
        "Man! I Feel Like A Woman! - Shania Twain",
        "Die a Happy Man - Thomas Rhett",
        "Wagon Wheel - Darius Rucker",
        "Girl Crush - Little Big Town",
        "Bless the Broken Road - Rascal Flatts",
    ],
    "blues": [
        "The Thrill Is Gone - B.B. King",
        "Hoochie Coochie Man - Muddy Waters",
        "Sweet Home Chicago - Robert Johnson",
        "Crossroads - Cream",
        "Stormy Monday - T-Bone Walker",
        "Born Under a Bad Sign - Albert King",
        "I Can't Quit You Baby - Led Zeppelin",
        "Pride and Joy - Stevie Ray Vaughan",
        "Red House - Jimi Hendrix",
        "Mary Had a Little Lamb - Buddy Guy",
        "I’m Your Hoochie Coochie Man - Muddy Waters",
        "Hellhound on My Trail - Robert Johnson",
        "Little Wing - Jimi Hendrix",
        "Texas Flood - Stevie Ray Vaughan",
        "Blues Hand Me Down - The Record Company",
    ],
    "soul": [
        "What's Going On - Marvin Gaye",
        "Ain't No Mountain High Enough - Marvin Gaye & Tammi Terrell",
        "Respect - Aretha Franklin",
        "I Heard It Through the Grapevine - Gladys Knight & The Pips",
        "Sittin' On The Dock of the Bay - Otis Redding",
        "Let's Stay Together - Al Green",
        "Midnight Train to Georgia - Gladys Knight & The Pips",
        "Lean on Me - Bill Withers",
        "I Say a Little Prayer - Aretha Franklin",
        "Superstition - Stevie Wonder",
        "Try a Little Tenderness - Otis Redding",
        "A Change Is Gonna Come - Sam Cooke",
        "You Are the Sunshine of My Life - Stevie Wonder",
        "I Want You Back - The Jackson 5",
        "Never Can Say Goodbye - Gloria Gaynor",
    ],
}


# Create the function for the dictionary
def main():
    print("Welcome to the Music Recommendation System!\n")
    print(
        "Here are the available genres you can explore: rock, pop, jazz, classical, hip hop, electronic, reggae, country, blues, soul."
    )
    # Ask the user what recommendations they want.

    user_input = (
        input("\nWhich music genre would you like recommendations for? ")
        .strip()
        .lower()
    )
    if user_input not in music_database:
        print(
            f"Oops! We couldn't find recommendations for the '{user_input}' genre. Try again with a different genre."
        )
        user_input = (
            input("\nWhich music genre would you like recommendations for? ")
            .strip()
            .lower()
        )
        if user_input not in music_database:
            print(
                f"Oops! We couldn't find recommendations for the '{user_input}' genre. Try again with a different genre or the program will end."
            )
            return
    recommendations = music_database[user_input]
    # Match with the key of the dictionaries. No room for errors.
    for key in music_database:
        if user_input == key:
            print(f"\nHere are some great {user_input} songs for you to enjoy:\n")
            for song in recommendations:
                print(f"- {song}")


# Run the program. Ask if they want to use it again or exit the program.
main()
while True:
    inp = (
        input(
            "Would you like to try another genre? Press 'Y' to restart or press 'N' to end.\n"
        )
        .strip()
        .lower()
    )
    if inp == "y":
        main()
    else:
        print("Thank you for using the Music Recommendation System.\n", "Good bye!")
        break

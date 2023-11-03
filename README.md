# HANGTHEMAN

HANGTHEMAN is an iteration of the so classical game of Hangman where the aim is to guess the word in it's whole or guessing letters one by one before you get hung, which in this case means 6 tries before you lose. 

To start playing the user guesses a letter or if they feel extra cocky they can always guess the word directly. Validation messages to point out when the user is doing an incorrect input is also available. 

It's fun and will prove to be a challenge, don't step away from it. 

![Home Screen]()

[View HANGTHEMAN live project here](https://hangtheman-5f8b3d25bf0d.herokuapp.com/)

- - -

## How to Play

The computer decides on a word that you then have to guess letter by letter or if possible the word in it's entirety straight away.
If you fail to do so you will lose and be hung while safety is in guessing the correct word. 

## User Experience (UX)

A very simple but oh so enjoyable game that is easy to get the hang of and spend time on. 
It's not more than blank spaces correlating with the amount of letters you should guess to win.

### User Stories

* First-time visitor goals
    * Understand the how-to-play part
    * Play it to test your guessing-skills

* Returning visitor goals
    * Keep on playing the game and challenge yourself
    * Share the experience

* Frequent user goals
    * Use as a type of party game or one of those games you play to waste time
    * Perfect your skills

- - -

## Features

* Computer chooses a random word
* Basic interface in black and white, good contrast
* Input functionality for letter/word
* Visual cues to track wrong guesses
* Win/Loss message at the end of game
* Play again possibilities

### Existing Features

* Intro screen (Logo and Intro copy)

![Intro Screen]()

* Ask user to make a guess

![Guess a letter]()

* Correct Guess

![Correct guess]()

* Incorrect Guess

![Incorrect guess]()

* Win

![Win]()

* Loss

![Loss]()

* Play again

![Play again]()

## Future features

* More words to expand possibilities
* Multiplayer - one picking word and one playing
* Scoreboard
* Difficulty
* Categories

- - -

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- - -

## Frameworks, Libraries & Programs Used

* [Codeanywhere](https://app.codeanywhere.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.

## Testing 

CI Python Linter was used to test run.py and random_words.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check]()
</details>

<details>
<summary> random_words.py CI Python Linter check
</summary>

![random_words.py linter check]()
</details>

## Manual Testing

Manual testing has been performed through the codeanywhere console throughout the project and furthermore when deployed to heroku.

| Feature | Result | Step | Works as intended |
| ------- | -------------- | ----------- | ------------- |
| Intro   | Logo and intro shown | None | :heavy_check_mark: |
| Guess a letter   | Ask user to guess a letter | None | :heavy_check_mark: |
| Correct Guess   | Display message of correct guess | Guessed a correct letter | :heavy_check_mark: |
| Incorrect Guess   | Display message of incorrect guess | Guessed an incorrect letter | :heavy_check_mark: |
| Invalid input/guess   | Display invalid input message | Invalid input | :heavy_check_mark: |
| Already guessed  | Display guessed already message | Guess same letter twice  | :heavy_check_mark: |
| Hangman steps   | Update hangman | Input a letter guess  | :heavy_check_mark: |
| Win   | Display win message | Guess the word | :heavy_check_mark: |
| Loss   | Display lose message | Fail to guess the word in six tries | :heavy_check_mark: |
| Play Again   | Display play again | Choose "YES" to play again and "NO" to end | :heavy_check_mark: |

## Input validation testing

* Guess a letter
    * Cannot continue with empty input
    * Must be a letter

* Play again
    * Cannot continue with empty input
    * Must be "YES" or "NO"


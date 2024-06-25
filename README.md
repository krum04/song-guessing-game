# Song Guessing Game

This is a simple song guessing game implemented in Python. Players listen to a short preview of a random song from a specified directory and try to guess the song title. The game uses fuzzy matching to check the similarity between the guessed title and the actual title.

## Features

- Multiple player support
- Random song selection
- Song preview playback
- Fuzzy matching for title guessing
- Score tracking

## Requirements

- Python 3.x
- `fuzzywuzzy` library
- `mutagen` library
- `mpv` media player

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/krum04/song-guessing-game.git
    cd song-guessing-game
    ```

2. Install the required Python libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Install `mpv` on your system. For Debian-based systems (like Ubuntu), you can use:
    ```sh
    sudo apt update
    sudo apt install mpv
    ```

## Usage

1. Place your `.mp3` files in the `./songs` directory.

2. Run the game:
    ```sh
    python song_guessing_game.py
    ```

3. Follow the prompts to enter the number of players, number of rounds, and preview length.

4. Listen to the song preview and guess the song title.

## Example

```sh
How many players? 2
How many rounds? 5
How long should the preview be? (1-10) 5
Enter player name: Alice
Enter player name: Bob
Player: Alice
Player: Bob
Song Playing
./songs/example_song.mp3
What is the song title? Example Title
Correct! 95%
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Acknowledgments

- [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy)
- [mutagen](https://mutagen.readthedocs.io/en/latest/)
- [mpv](https://mpv.io/)

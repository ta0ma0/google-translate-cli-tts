# Google Translate CLI with TTS via fastspeech2-en-ljspeech

## Instalation

1. Clone the repository: git clone https://github.com/yourusername/google-translate-cli.git
2. Install the required dependencies: pip install -r requirements.txt

## Usage

To use the tool, run the following command:

```
python app.py [text] [-l] [-ln] [-lang]

```

- [text] (required): The text that you want to translate.
- -l or --loud (optional): Plays the translated text as a sound.
- -ln or --langs (optional): Prints a list of supported languages.
- -lang or --chooselang (optional): Specifies the target language for translation.

Defaults to en_US.
Example usage:

```
python app.py "Hello, world!" -lang fr_FR

```

## Supported Languages

To see a list of supported languages, run the following command

```
python app.py --langs

```

## Configuration

You must setting up you Google API (via gcloud). Before running the tool, make sure to set the PROJECT_ID environment variable to your Google Cloud project ID. 

```
export PROJECT_ID=your-project-id

```

## Playing the Translated Text

To play the translated text as a sound, use the -l or --loud flag:

```
python app.py "Hello, world!" -l

```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

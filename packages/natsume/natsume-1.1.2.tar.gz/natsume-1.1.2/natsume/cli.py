import argparse
import fileinput

from .nat import Natsume
from .dict import DICT_URLS

dict_names = list(DICT_URLS.keys())

def main():
    """Wrapper to use natsume from command line.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--function", 
                        type=str, choices=["g2p", "tokenize", "mecab", "njd"], default="g2p",
                        help="Function to use")
    parser.add_argument("-d", "--dict_name",
                        type=str, choices=dict_names, default=dict_names[0],
                        help="Dictionary name")
    parser.add_argument("-N", "--nbest",
                        type=int, default=1,
                        help="Return N best results")
    parser.add_argument("-p", "--phoneme",
                        type=str, choices=["romaji", "ipa"], default="romaji",
                        help="Phonemization mode")
    parser.add_argument("-t", "--token",
                        type=str, choices=["word", "phrase"], default="phrase",
                        help="Tokenization mode")
    parser.add_argument("-m", "--model",
                        type=str, choices=["rule", "marine"], default="rule",
                        help="Model to predict accent sandhi")
    parser.add_argument("-a", "--accent",
                        type=bool, choices=[True, False], default=False,
                        help="Output with accent")

    args = parser.parse_args()

    nat = Natsume(dict_name=args.dict_name)

    for line in fileinput.input([]):
        if args.function == "g2p":
            results_list = nat.g2p_nbest(text=line, 
                                         phoneme_mode=args.phoneme, token_mode=args.token,
                                         with_accent=args.accent, model=args.model, num=args.nbest)
            print_natsume(results_list=results_list, mode="g2p")
        elif args.function == "tokenize":
            results_list = nat.tokenize_nbest(text=line,
                                              mode=args.token, model=args.model, num=args.nbest)
            print_natsume(results_list=results_list, mode="tokenize")
        elif args.function == "mecab":
            results_list = nat.get_mecab_features_nbest(text=line, num=args.nbest)
            print_natsume(results_list=results_list, mode="mecab")
        elif args.function == "njd":
            results_list = nat.get_njd_features_nbest(text=line, num=args.nbest)
            print_natsume(results_list=results_list, mode="njd")
        
def print_g2p(phonemes_list: list):
    """Print g2p results.

    Args:
        phoneme_list (list): Phonemes_list.
    """

    for i, phonemes in enumerate(phonemes_list):
        print("result {}:".format(i + 1))
        phonemes = " ".join(phonemes)
        print(phonemes)

def print_tokenize(tokens_list: list):
    """Print tokenization results.

    Args:
        tokens_list (list): Tokens list.
    """

    for i, tokens in enumerate(tokens_list):
        print("result {}:".format(i + 1))
        tokens = [token.surface() for token in tokens]
        tokens = " ".join(tokens)
        print(tokens)

def print_mecab(features_list: list):
    """Print MeCab results.

    Args:
        features_list (list): MeCab features list.
    """

    for i, features in enumerate(features_list):
        print("result {}:".format(i + 1))
        for feature in features:
            surface = feature["surface"]
            feats = [str(feat) for feat in list(feature.values())[1:]]
            feature_string = ",".join(feats)
            print("{}\t{}".format(surface, feature_string))

def print_njd(features_list: list):
    """Print NJD results.

    Args:
        features_list (list): NJD features list.
    """

    for i, features in enumerate(features_list):
        print("result {}:".format(i + 1))
        for feature in features:
            surface = feature["surface"]
            feats = [str(feat) for feat in list(feature.values())[1:]]
            feature_string = ",".join(feats)
            print("{}\t{}".format(surface, feature_string))

def print_natsume(results_list: list, mode: str):
    """Print function for using natsume from command line.

    Args:
        results_list (list): Results list.
        mode (str): Function mode.
    """

    if mode == "g2p":
        print_g2p(phonemes_list=results_list)
    elif mode == "tokenize":
        print_tokenize(tokens_list=results_list)
    elif mode == "mecab":
        print_mecab(features_list=results_list)
    elif mode == "njd":
        print_njd(features_list=results_list)
    else:
        raise ValueError("Not supported mode {}.".format(mode))
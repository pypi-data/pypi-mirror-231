from .dict import DictManager
from .mecab import MecabTagger
from .njd import NJDPredictor
from .utils import MecabFeature, NJDFeature, merge_njd_marine_features, feature_to_string


class Frontend(object):
    def __init__(self, dict_name=None):
        self._dict_name = dict_name
        self._tagger = None     # mecab tagger
        self._njd = None        # njd predictor
        self._marine = None     # marine predictor
        self._dm = None         # dictionary manager

        self._initialize()

    def _initialize(self):
        self._njd = NJDPredictor()
        self._dm = DictManager()

        # Initialize marine
        # Reference: https://github.com/r9y9/pyopenjtalk/blob/master/pyopenjtalk/__init__.py
        try:
            from marine.predict import Predictor as MarinePredictor
        except BaseException:
            raise ImportError(
                "marine is not installed! Please see {} for more information."
                .format("https://github.com/6gsn/marine")
            )
        
        self._marine = MarinePredictor()
        dict_dir = self._dm.get_dict_dir(self._dict_name)
        self._tagger = MecabTagger(dicdir=dict_dir)

    def set_dict_dir(self, dict_dir):
        self._dict_dir = dict_dir
        self._initialize()

    def get_features(self, text, mode="word", model="rule"):
        features_list = self.get_features_nbest(text, mode=mode, model=model, num=1)
        
        return features_list[0]

    def get_features_nbest(self, text, mode="word", model="rule", num=1):
        features_list = []
        if mode == "word":
            raw_features_list = self.get_mecab_features_nbest(text, num=num)
            for raw_features in raw_features_list:
                # for every lattice
                features = []
                for raw_feature in raw_features:
                    feature = MecabFeature(raw_feature)
                    features.append(feature)
                features_list.append(features)

        elif mode == "phrase":
            if model == "rule":
                # default is rule-based model
                raw_features_list = self.get_njd_features_nbest(text, num=num)
            elif model == "marine":
                # accent sandhi estimation using marine
                from marine.utils.openjtalk_util import convert_njd_feature_to_marine_feature

                raw_features_list = []
                njd_features_list = self.get_njd_features_nbest(text, num=num)
                for njd_features in njd_features_list:
                    marine_features = convert_njd_feature_to_marine_feature(njd_features)
                    marine_results = self._marine.predict(
                        [marine_features], require_open_jtalk_format=True
                    )
                    raw_features = merge_njd_marine_features(njd_features, marine_results)
                    raw_features_list.append(raw_features)
            else:
                # default is rule-based model
                raw_features_list = self.get_njd_features_nbest(text, num=num)

            # raw feature to njd feature
            for raw_features in raw_features_list:
                features = []
                for raw_feature in raw_features:
                    feature = NJDFeature(raw_feature)
                    features.append(feature)
                features_list.append(features)

        return features_list

    def get_mecab_features(self, text):
        features = self._tagger.parse(text)

        return features
    
    def get_mecab_features_nbest(self, text, num=1):
        features_list = self._tagger.parse_nbest(text, num)

        return features_list
    
    def get_njd_features(self, text):
        features_list = self.get_njd_features_nbest(text, num=1)

        return features_list[0]

    def get_njd_features_nbest(self, text, num=1):
        mecab_features_list = self._tagger.parse_nbest(text, num=num)
        features_list = []
        for mecab_features in mecab_features_list:
            feature_strings = []
            for mecab_feature in mecab_features:
                feature_string = feature_to_string(mecab_feature)
                feature_strings.append(feature_string)
            features = self._njd.predict(feature_strings)
            features_list.append(features)

        return features_list
    
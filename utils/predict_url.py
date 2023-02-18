import joblib
from lightgbm.sklearn import LGBMClassifier
from .tools import use_of_ip, count_dot, count_www, count_dog, count_dir, embeded_domains, short_url, count_https, \
    count_min, count_ask, count_per, count_rav, count_http, url_len, hostname_len, sus_url, count_dig, count_let


class Predict:

    def __init__(self, url: str):
        self._filename = "models/my_model.pkl"
        self._url = url

    def _unfolding_the_model(self) -> LGBMClassifier:
        self.model = joblib.load("models/my_model.pkl")
        return self.model

    def _signs_pred(self) -> list[list[int]]:
        self.signs_pred = [[use_of_ip(self._url), count_dot(self._url), count_www(self._url), count_dog(self._url),
                            count_dir(self._url), embeded_domains(self._url), short_url(self._url),
                            count_https(self._url),
                            count_http(self._url), count_per(self._url), count_ask(self._url), count_min(self._url),
                            count_rav(self._url), url_len(self._url), hostname_len(self._url), sus_url(self._url),
                            count_dig(self._url), count_let(self._url)]]
        return self.signs_pred

    def predict_url(self) -> str:
        self._signs_pred()
        self._unfolding_the_model()
        return self.model.predict(self.signs_pred)

# p = Predict('www.youtube.com')
#
# print(p.predict_url())

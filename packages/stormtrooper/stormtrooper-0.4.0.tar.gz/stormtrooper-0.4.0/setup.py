# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stormtrooper']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.0,<2.0.0',
 'scikit-learn>=1.2.0,<2.0.0',
 'thefuzz>=0.18.0,<0.19.0',
 'tqdm>=4.60.0,<5.0.0',
 'transformers>=4.25.0,<5.0.0']

extras_require = \
{'openai': ['openai>=0.28.0,<0.29.0', 'tiktoken>=0.5.0,<0.6.0'],
 'setfit': ['setfit>=0.7.0,<0.8.0', 'datasets>=2.14.0,<3.0.0'],
 'torch': ['torch>=2.0.0,<3.0.0']}

setup_kwargs = {
    'name': 'stormtrooper',
    'version': '0.4.0',
    'description': 'Transformer/LLM-based zero and few-shot classification in scikit-learn pipelines',
    'long_description': '<img align="left" width="82" height="82" src="assets/logo.svg">\n\n# stormtrooper\n\n<br>\nTransformer-based zero/few shot learning components for scikit-learn pipelines.\n\n[Documentation](https://centre-for-humanities-computing.github.io/stormtrooper/)\n\n## New in version 0.4.0 :fire:\n\n- You can now use OpenAI\'s chat models with blazing fast :zap: async inference.\n\n## New in version 0.3.0 🌟 \n\n- SetFit is now part of the library and can be used in scikit-learn workflows.\n\n## Example\n\n```bash\npip install stormtrooper\n```\n\n```python\nclass_labels = ["atheism/christianity", "astronomy/space"]\nexample_texts = [\n    "God came down to earth to save us.",\n    "A new nebula was recently discovered in the proximity of the Oort cloud."\n]\n```\n\n\n### Zero-shot learning\n\nFor zero-shot learning you can use zero-shot models:\n```python\nfrom stormtrooper import ZeroShotClassifier\nclassifier = ZeroShotClassifier().fit(None, class_labels)\n```\n\nGenerative models (GPT, Llama):\n```python\nfrom stormtrooper import GenerativeZeroShotClassifier\n# You can hand-craft prompts if it suits you better, but\n# a default prompt is already available\nprompt = """\n### System:\nYou are a literary expert tasked with labeling texts according to\ntheir content.\nPlease follow the user\'s instructions as precisely as you can.\n### User:\nYour task will be to classify a text document into one\nof the following classes: {classes}.\nPlease respond with a single label that you think fits\nthe document best.\nClassify the following piece of text:\n\'{X}\'\n### Assistant:\n"""\nclassifier = GenerativeZeroShotClassifier(prompt=prompt).fit(None, class_labels)\n```\n\nText2Text models (T5):\nIf you are running low on resources I would personally recommend T5.\n```python\nfrom stormtrooper import Text2TextZeroShotClassifier\n# You can define a custom prompt, but a default one is available\nprompt = "..."\nclassifier =Text2TextZeroShotClassifier(prompt=prompt).fit(None, class_labels)\n```\n\n```python\npredictions = classifier.predict(example_texts)\n\nassert list(predictions) == ["atheism/christianity", "astronomy/space"]\n```\n\nOpenAI models:\nYou can now use OpenAI\'s chat LLMs in stormtrooper workflows.\n\n```python\nfrom stormtrooper import OpenAIZeroShotClassifier\n\nclassifier = OpenAIZeroShotClassifier("gpt-4").fit(None, class_labels)\n```\n\n```python\npredictions = classifier.predict(example_texts)\n\nassert list(predictions) == ["atheism/christianity", "astronomy/space"]\n```\n\n### Few-Shot Learning\n\nFor few-shot tasks you can only use Generative, Text2Text, OpenAI (aka. promptable) or SetFit models.\n\n```python\nfrom stormtrooper import GenerativeFewShotClassifier, Text2TextFewShotClassifier, SetFitFewShotClassifier\n\nclassifier = SetFitFewShotClassifier().fit(example_texts, class_labels)\npredictions = model.predict(["Calvinists believe in predestination."])\n\nassert list(predictions) == ["atheism/christianity"]\n```\n\n### Fuzzy Matching\n\nGenerative and text2text models by default will fuzzy match results to the closest class label, you can disable this behavior\nby specifying `fuzzy_match=False`.\n\nIf you want fuzzy matching speedup, you should install `python-Levenshtein`.\n\n### Inference on GPU\n\nFrom version 0.2.2 you can run models on GPU.\nYou can specify the device when initializing a model:\n\n```python\nclassifier = Text2TextZeroShotClassifier(device="cuda:0")\n```\n',
    'author': 'Márton Kardos',
    'author_email': 'power.up1163@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

my_text = """The Advertisement was telecasted nationwide, and the product was sold in around 30 states of America. The product became so successful among the people that the production was increased. Two new plant sites were finalized, and the construction was started. Now, The Cloud Enterprise became one of America's biggest firms and the mass producer in all major sectors, from transportation to personal care. Director of The Cloud Enterprise, Ryan Cloud, was now started getting interviewed over his success stories. Many popular magazines were started publishing Critiques about him."""  

print(sent_tokenize(my_text))


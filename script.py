import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print np.mean(rottweiler_tl)
print np.std(rottweiler_tl)

#Are whippets significantly more or less likely to be a rescue?
whippet_rescue = fetchmaker.get_is_rescue('whippet')
#No. of whippets that are rescues
num_whippet_rescues = np.count_nonzero(whippet_rescue)
#Total no. of whippets
num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippet_rescues, n=num_whippets, p=0.08)
print pval #0.58
#The result is not significant. Whippets are not more likely to be rescues.

#Is there a significant difference in the average weights of 3 dog breeds(whippets, terriers, and pitbulls)?
whippet = fetchmaker.get_weight('whippet')
terrier = fetchmaker.get_weight('terrier')
pitbull = fetchmaker.get_weight('pitbull')

fstat, pval = f_oneway(whippet, terrier, pitbull)
print pval #3.27641558827e-17
#Which of the pairs of these dog breeds differ from each other?
dog_breeds = np.concatenate([whippet, terrier, pitbull])
labels = ['whippet'] * len(whippet) + ['terrier'] * len(terrier) + ['pitbull'] * len(pitbull)
tukey_results = pairwise_tukeyhsd(dog_breeds, labels, 0.05)
print tukey_results #There is a significant difference between the average weights of the pitbull and whippet.

#Categorical dog test. We want to see if poodles and shihtzu have significantly different color breakdowns
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
#Get no. of brown poodles
black_poodle = np.count_nonzero(poodle_colors == 'black')
brown_poodle = np.count_nonzero(poodle_colors == 'brown')
gold_poodle = np.count_nonzero(poodle_colors == 'gold')
grey_poodle = np.count_nonzero(poodle_colors == 'grey')
white_poodle = np.count_nonzero(poodle_colors == 'white')
print black_poodle, brown_poodle, gold_poodle, grey_poodle, white_poodle #17,13,8,52,10
black_shihtzu = np.count_nonzero(shihtzu_colors == 'black')
brown_shihtzu = np.count_nonzero(shihtzu_colors == 'brown')
gold_shihtzu = np.count_nonzero(shihtzu_colors == 'gold')
grey_shihtzu = np.count_nonzero(shihtzu_colors == 'grey')
white_shihtzu = np.count_nonzero(shihtzu_colors == 'white')
print black_shihtzu, brown_shihtzu, gold_shihtzu, grey_shihtzu, white_shihtzu #10,36,6,41,7

color_table =[[17,10], [13,36], [8,6], [52,41], [10,7]]
chi2, pvalue, dof, expected = chi2_contingency(color_table)
print pvalue #0.00530240829324
#Therefore there is no significant difference in the color breakdowns between poodles and shihtzu.

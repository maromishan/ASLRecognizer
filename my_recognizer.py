import warnings
from asl_data import SinglesData


def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    all_Xlengths = test_set.get_all_Xlengths()
    all_seqs = test_set.get_all_sequences()
    #item_seqs = test_set.get_item_sequences() - wrong need to pass in item parameter
    #item_Xlengths = test_set.get_item_Xlengths()

    for id in range(0, len(all_Xlengths)):
      #Look at each word individually
      test_x, test_Xlength = test_set.get_item_Xlengths(id)
      pdict = {}

      #calculate logLs
      #for word, model in models.items():
      for word in models:
        #try:
          logL = models.score(test_x, test_Xlength)
          pdict[word] = logL
        #except:
          #source: https://discussions.udacity.com/t/my-recognizer-error/539064
          pdict[word] = float('-inf')

    guesses.append(max(pdict.items(), key = lambda x: x[1])[0])
    probabilities.append(pdict)
    print('here')



      #Choose optimal model
        #best_model = float('-inf')
        #best_guess = None


        #for i in pdict:
            #if pdict[i] > best_model:
                #best_model = pdict[i]
                #best_guess = i
            #guesses.append(best_guess)



    print(guesses)
    print(probabilities)

    return (probabilities, guesses)

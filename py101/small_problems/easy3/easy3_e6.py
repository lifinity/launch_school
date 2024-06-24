# madlibs
# create a simple madlib program that prompts for noun, verb, adverb & adjective
# and injects them into a templated story

# import re

def madlibs(story=None):
    delimiter = '|'
    def delimiterize(str_, delim=delimiter):
        return delim + str_ + delim

    noun_key = delimiterize("noun")
    verb_key = delimiterize("verb")
    adverb_key = delimiterize("adverb")
    adj_key = delimiterize("adjective")
    blanks_list = [noun_key, verb_key, adverb_key, adj_key]

    story = f"There once was a {adj_key} {noun_key} who loved " \
          + f"to {verb_key} {adverb_key}.\nOne day the wind {verb_key}'d " \
          + f"the {noun_key} {adverb_key} to the {adj_key} spring,\nwhere " \
          + f"they found a whole group of {noun_key}s who were far more \n" \
          + f"{adj_key} and {adverb_key} {verb_key}'ing than they." \
          if not story else story

    '''
    # this is if you wanted to enter diff input for every blank but you'd
    # also have to make sure story.replace() only replaces 1 instance
    pattern_str = fr"{re.escape(noun_key)}|{re.escape(verb_key)}" \
                + fr"|{re.escape(adverb_key)}|{re.escape(adj_key)}"
    
    blanks_list = re.findall(pattern_str, story)
    '''

    for key in blanks_list:
        val = input(f"Enter {key.strip(delimiter)}: ")
        
        while not val.isalpha():
            print("Invalid input. Alphabetical words only.")
            val = input(f"Enter {key.strip(delimiter)}: ")
        
        story = story.replace(key, val)
    
    print(story)

# official solution was a lot more straightforward & directly used the variables
# capturing user input in the formatted string; mine honestly over-engineered
# but it did force knowledge upon me.

# NOTABLY: be careful of unwanted substr replacement when using str.replace()
# can get around w/ delimiters or regex's \b, but be wary of that too when you
# expect/want certain boundaries, e.g. {verb_key}ed doesn't match {verb_key}\b
# also make sure to re.escape() your match variables if special chars like '|'

madlibs()
# madlibs("A |adjective| |noun| just |adverb| |verb|'d everything.")
    
    
  
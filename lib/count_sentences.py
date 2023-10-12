#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value=''):
    self.string_value = value


  def get_value(self):
    return self.string_value
  
  def set_value(self, value):
    if (type(value) == str):
      self.string_value = value
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)


  def is_sentence(self):
    if self.string_value.endswith('.'):
      return True
    else:
      return False
    

  def is_question(self):
    if self.string_value.endswith('?'):
      return True
    else:
      return False


  def is_exclamation(self):
    if self.string_value.endswith('!'):
      return True
    else:
      return False
    

  def count_sentences(self):
    value = self.value
    for punct in ['!', '?']:
      value = value.replace(punct, '.')
      sentences = []
      for sentence in value.split('.'):
        if sentence:
          sentences.append(sentence)

    return len(sentences)
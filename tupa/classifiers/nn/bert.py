import numpy as np
import tensorflow as tf

from .sub_model import SubModel

class Bert(SubModel):
	'''
	Implementation of BERT.
	'''
	def __init__(self, params = None, save_path = (), shared = False, copy_shared = False):
		print('You are in BERT implementation class.')
		return super().__init__(params, save_path, shared, copy_shared)

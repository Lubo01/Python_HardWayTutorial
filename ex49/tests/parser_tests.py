from nose.tools import *
from ex49 import ex49

def test_init():
	test_class = ex49.Sentence(('direction','west'),('verb','go'),('noun','bear'))
		
	assert_equal(test_class.verb, 'go')
	assert_equal(test_class.subject, 'west')
	
def test_peek():
	assert_equal(ex49.peek ([('noun','bear'),('verb','go')]), 'noun')

def test_match():
	assert_equal(ex49.match ([('noun','bear'),('verb','go')],'noun'), ('noun','bear'))
	
def test_skip():
	assert_equal(ex49.skip ([('noun','bear'),('verb','go')],'stop'), None)
	
	
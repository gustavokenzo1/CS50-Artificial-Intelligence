import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """    

    # Create dict to store all linked pages and their probabilities
    possible_pages = dict()
    # Get amount of links from the current page and amount of page of currrent corpus
    links = len(corpus[page])
    pages = len(corpus)

    for p in corpus.keys():
        additional = 0
        if p in corpus[page]:
            additional = damping_factor / links
        if links == 0:
            additional = damping_factor / pages
        possible_pages[p] = (1 - damping_factor)/pages + additional
    return possible_pages

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Firstly, select a random page
    page = random.choice(list(corpus.keys()))
    pageranks = dict()

    # Store all pages from corpus in a dict, starting with probability 0
    for p in corpus:
        pageranks[p] = 0

    samples = 1 # Start with 1 so we don't divide by 0 later on
    N = n

    # While loop to go through the process n times
    while n > 0:
        # Recursively change current dict by calling transition_model() 
        new = transition_model(corpus, page, damping_factor)

        # For every page in current corpus, we add more probability 
        # Each single probability is very low, since we divide by an increasing amount of samples
        # Simply put, it's like we have an initial probability, and we increase it N times, then
        # we divide by N
        for p in pageranks:
            pageranks[p] = ((samples - 1) * pageranks[p] + new[p]) / samples

        # Randomly chose a new page to continue the loop by using weights
        page = random.choices(list(new.keys()), list(new.values()))[0]
        # Guarantee we don't have an infinite loop
        n -= 1
        samples += 1

        # When done, return dict
        if samples == N:
            return pageranks
    

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    
    # The function should begin by assigning each page a rank of 1 / N, 
    # where N is the total number of pages in the corpus.

    rank = dict()
    n = len(corpus)

    for p in corpus:
        rank[p] = 1 / n

    # PR(p) = (random page) v (from page i to page p)
    # v = or
    # In probability, or = +
    
    # We need to do it recursively, till the values converges, so we do a while loop
    while True:
        counter = 0
        for p in corpus:
            # PageRank starts with a constant value, which is from random page with probability 1 - d
            pr = (1 - damping_factor) / n
            # Second element of the formula is from page i to page p, start with 0
            pr2 = 0
            for page in corpus:
                # If p is in a page's links, use the formula
                if p in corpus[page]:
                    num_links = len(corpus[page])
                    # Keep summing (sigma)
                    pr2 += (rank[page] / num_links)
            # After sums, multiply by d
            pr2 *= damping_factor
            # Then add up everything to the main formula
            pr += pr2
            
            # Check the precision until it is less than 0.001
            if rank[p] > pr:
                if (rank[p] - pr) < 0.001:
                    counter += 1
            else:
                if (pr - rank[p]) < 0.001:
                    counter += 1
            rank[p] = pr

        if counter == n:
            break
    return rank

if __name__ == "__main__":
    main()
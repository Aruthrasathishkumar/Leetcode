from collections import Counter
import heapq


def top_k_words(filename, k):
    """Find top k most frequent words in a file."""
    
    word_count = Counter()

    with open(filename, 'r') as f:
        for line in f:
            # Clean and split line
            words = line.lower().split()
            for word in words:
                # Remove punctuation
                cleaned = ''.join(c for c in word if c.isalnum())
                if cleaned:
                    word_count[cleaned] += 1

    # Get top k using heap
    return heapq.nlargest(k, word_count.items(), key=lambda x: x[1])


# For very large files: MapReduce approach

def map_phase(chunk):
    """Map phase: count words in a chunk of lines."""
    
    local_count = Counter()

    for line in chunk:
        words = line.lower().split()
        for word in words:
            cleaned = ''.join(c for c in word if c.isalnum())
            if cleaned:
                local_count[cleaned] += 1

    return local_count


def reduce_phase(counters):
    """Reduce phase: combine multiple Counter objects."""
    
    total_count = Counter()

    for counter in counters:
        total_count.update(counter)

    return total_count
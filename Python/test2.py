def solve():
  import sys
  read = sys.stdin.read
  data = read().split()

  N, X = int(data[0]), int(data[1])
  P = list(map(int, data[2:]))

  # Convert probabilities to fractions
  prob = [p / 100 for p in P]

  # Probability distribution of rare cards in one pack
  max_cards = N
  pack_prob = [0] * (max_cards + 1)
  pack_prob[0] = 1  # Probability of 0 rare cards initially

  for p in prob:
    next_prob = [0] * (max_cards + 1)
    for j in range(max_cards + 1):
      if j > 0:
        next_prob[j] += pack_prob[j - 1] * p
      next_prob[j] += pack_prob[j] * (1 - p)
    pack_prob = next_prob

  # Expected number of packs to collect at least X rare cards
  dp = [float('inf')] * (X + 1)
  dp[0] = 0  # Base case: 0 packs needed for 0 rare cards

  for k in range(1, X + 1):
    expected_packs = 0
    prob_sum = 0
    for i in range(min(k, N) + 1):
      if k - i >= 0:
        expected_packs += pack_prob[i] * dp[k - i]
        prob_sum += pack_prob[i]
    dp[k] = (expected_packs + 1) / prob_sum

  print(f"{dp[X]:.12f}")
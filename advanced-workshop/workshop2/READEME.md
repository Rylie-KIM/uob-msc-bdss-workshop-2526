# Generated from Grok3 - 26-Nov-2025 

## 1. Data Preparation Pipeline
- Gopher filtering → high-quality document filtering used in DeepMind’s Gopher and almost every modern dataset (FineWeb, etc.)
- MinHash deduplication (a.k.a. “Minhas dedup”) → exact & near-duplicate removal using LSH
- FineWeb → 15 trillion token open dataset from Hugging Face (cleaned Common Crawl with the above two techniques)

## 2. Tokenization 101
- Why we need it: turn text → fixed-length integer IDs that the model can compute on
- BPE (Byte Pair Encoding) = repeatedly merge the most frequent pair of bytes/subwords → creates vocab of ~32k–128k tokens
- Token IDs are simply sorted by frequency (lower ID = more frequent token)
- Fatal weaknesses:
  - One logical word → multiple tokens (e.g. “Sutskever” → “Sut”+“skever” → spelling mistakes)
  - Extremely poor at counting letters/numbers because of token boundaries

## 3. Transformer Architecture (still the king in 2025)
- Embedding + Positional Encoding → Multi-Head Self-Attention + Feed-Forward → stack 32–128 layers
- RoPE (Rotary Positional Embedding) = current standard for positional info (LLaMA, Grok, Mistral, Gemma, etc.)

## 4. How LLMs Actually Learn (full life cycle)
1. Pre-training: next-token prediction on ~15T tokens
2. SFT (Supervised Fine-Tuning): learn from ~100k–1M (question → good answer) pairs
3. RLHF / PPO: align with human preferences using a separate Reward Model

## 5. Why answers are never 100% identical
1. Temperature / top-p / top-k sampling (70–80% of the variance)
2. Random seed
3. Tokenization differences (very minor)

temperature = 0.0 → deterministic, same answer every time

## 6. Special tokens for chat structure
```text
<|system|>…<|end|>
<|user|>Hello<|end|>
<|assistant|>Hi!<|end|>
```
→ without these the model cannot tell who is speaking.

## 7. Korean token nightmare
- Korean uses 2.5–3.5× more tokens than English for the same meaning
- Because of spacing, particles, and Hangul syllable structure

## 8. History of text models
- ~2018: RNN / LSTM / CNN
- 2018~now: Transformer completely dominates (RNN papers basically extinct)

## 9. Reinforcement Learning (RLHF/PPO) logic
1. Policy πθ (the LLM) generates a full answer
2. Separate Reward Model scores it (e.g. +8.7 or –4.1)
3. Compute advantage
4. Update policy with clipped PPO objective
5. Repeat millions of times

Reward Model is a completely separate network (usually same size as the policy) and is discarded after training.

## 10. Best-of-N / “Take the top solution”
- Generate N=16–64 answers with current policy
- Let RM score them
- Train (or reinforce) only on the highest-scoring one(s)
→ this is why o1, Claude 3.5, LLaMA-3.1 405B, Qwen2-Math, DeepSeek-Math all reach 98–99% on GSM8K

## Final takeaway (2025)
Everything that is not a toy model today is:
Transformer → Pre-train → SFT → separate Reward Model + PPO (often with Best-of-N) → final chat model

That’s it.  
Now I can finally sleep. Good night!
# Digit GIFs

These GIFs are used as the answer numbers in the quiz.

## Trimming (remove extra space around digits)

To crop transparent or uniform padding so numbers sit close together when displayed:

```bash
# From the quiz-collector folder:
pip install -r requirements.txt
python3 trim_gifs.py
```

This overwrites each `0.gif`–`9.gif` with a trimmed version. Back up the originals first if needed.

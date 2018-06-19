# Twitter-Emotion-Analyzer

This program will analyze the sentiment level of the person who tweets about
a specific topic and will give out a user friendly score to the user about
the tweets sentiment level.

This Program intends to showcase a glimpse of common natural language processing (NLP)

## How Sentiment is scored

Polarity and Subjectivity can be calculated using the TextBlob library. Polarity is how negative or postive a sentence is. Subjectivity is how objective ( An objective perspective is one that is not influenced by emotions, opinions, or personal feelings - it is a perspective based on fact, in things quantifiable and measurable) or subjective (A subjective perspective is one open to greater interpretation based on personal feeling, emotion, aesthetics, etc.) a sentence is.

The polarity score is a float within the range [-1.0, 1.0] where -1.0 is very negative and 1.0 is very positive. The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
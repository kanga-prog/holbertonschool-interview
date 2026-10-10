#include <stdlib.h>
#include "substring.h"

/**
 * str_len - returns the length of a string
 * @str: string to measure
 *
 * Return: length of the string
 */
static int str_len(const char *str)
{
	int len = 0;

	while (str[len])
		len++;

	return (len);
}

/**
 * word_match - compares a portion of a string with a word
 * @s: string portion
 * @word: word to compare
 * @len: number of characters to compare
 *
 * Return: 1 if equal, otherwise 0
 */
static int word_match(const char *s, const char *word, int len)
{
	int i;

	for (i = 0; i < len; i++)
	{
		if (s[i] != word[i])
			return (0);
	}

	return (1);
}

/**
 * valid_substring - checks if a substring contains every word exactly once
 * @s: beginning of the substring
 * @words: array of words
 * @nb_words: number of words
 * @word_len: length of each word
 *
 * Return: 1 if valid, otherwise 0
 */
static int valid_substring(const char *s, const char **words,
			   int nb_words, int word_len)
{
	int *used;
	int i, j, found;

	used = malloc(sizeof(int) * nb_words);
	if (used == NULL)
		return (0);

	for (i = 0; i < nb_words; i++)
		used[i] = 0;

	for (i = 0; i < nb_words; i++)
	{
		found = 0;

		for (j = 0; j < nb_words; j++)
		{
			if (!used[j] &&
			    word_match(s + (i * word_len), words[j], word_len))
			{
				used[j] = 1;
				found = 1;
				break;
			}
		}

		if (!found)
		{
			free(used);
			return (0);
		}
	}

	free(used);
	return (1);
}

/**
 * find_substring - finds substrings made from all given words
 * @s: string to scan
 * @words: array of words
 * @nb_words: number of words
 * @n: address where the number of matches is stored
 *
 * Return: allocated array of starting indices, or NULL
 */
int *find_substring(char const *s, char const **words, int nb_words, int *n)
{
	int *indices;
	int s_len, word_len, substring_len;
	int i, count = 0;

	*n = 0;

	if (s == NULL || words == NULL || nb_words <= 0 || words[0] == NULL)
		return (NULL);

	word_len = str_len(words[0]);
	if (word_len == 0)
		return (NULL);

	s_len = str_len(s);
	substring_len = word_len * nb_words;

	if (substring_len > s_len)
		return (NULL);

	indices = malloc(sizeof(int) * (s_len - substring_len + 1));
	if (indices == NULL)
		return (NULL);

	for (i = 0; i <= s_len - substring_len; i++)
	{
		if (valid_substring(s + i, words, nb_words, word_len))
			indices[count++] = i;
	}

	if (count == 0)
	{
		free(indices);
		return (NULL);
	}

	*n = count;
	return (indices);
}

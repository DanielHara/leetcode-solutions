/*
    Question 3475: https://leetcode.com/problems/dna-pattern-recognition/

    Just do it, should be an easy question
*/

# Write your MySQL query statement below

SELECT sample_id, dna_sequence, species, (dna_sequence LIKE 'ATG%') AS has_start, (dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA') AS has_stop, (dna_sequence LIKE '%ATAT%') AS has_atat, (dna_sequence LIKE '%GGG%') AS has_ggg from Samples ORDER BY sample_id ASC

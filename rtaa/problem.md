# Problem
1. banyak transcription yang tidak berhasil ke save di bigquery
(LLM bisa predict the number, but there is no number in the transcription)
2. slow processing time, until 90 seconds still unknown
3. accuracy input google STT di jogja dan semarang sangat buruk dibandingkan jakarta

# SOLUTION
1. proper logging when hit LLM, save to big query, download data from GCS
2. need performance testing using k6, to mock concurrent situation 
3. membandingkan transcription google STT vs transcription qapm
4. posibble enggak nambahin fullstop di google stt, apakah google STT punya fitur untuk fullstop?


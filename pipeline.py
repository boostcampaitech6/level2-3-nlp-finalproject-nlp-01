import librosa 


from youtube2audio import downloadYouTube, convertVideo2Audio
from text2summ import *
from audio2text import convertAudio2Text


if __name__ == '__main__':
    youtube_link='https://www.youtube.com/watch?v=e0V1CtzFgrU'
    video_dir=youtube_link.split('watch?v=')[1]

    # downloadYouTube(youtube_link, f_name=video_dir)
    # convertVideo2Audio(f"videos/{video_dir}.mp4")

    sample, sampling_rate = librosa.load(f'videos/{video_dir}.mp3')    
    output = convertAudio2Text(sample)
    print(output)

    # MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"
    # cache_dir = "/data/ephemeral/Youtube-Short-Generator/models/mistral"

    # tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME,cache_dir=cache_dir)
    # tokenizer.pad_token_id = tokenizer.eos_token_id
    # model = AutoModelForCausalLM.from_pretrained(
    #     MODEL_NAME,
    #     cache_dir=cache_dir)
    # pipe = pipeline(
    #     "text-generation", 
    #     model=model, 
    #     tokenizer=tokenizer, 
    #     max_new_tokens=args.max_new_token, 
    #     device = 0, 
    #     pad_token_id=tokenizer.eos_token_id)
    # hf = HuggingFacePipeline(pipeline=pipe)

    # sample = dataset.sample(n)
    # result_df = get_summarization(sample, save_name, lower, upper, config['data_name'][args.data_num],iter)

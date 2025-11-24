from script_generator import generate_script
from animation_generator import generate_animation
from voice_generator import generate_voice
from uploader import upload_to_youtube

def run_daily_agent():

    # Step 1 — Generate Script
    script = generate_script()
    print("SCRIPT READY:\n", script)

    # Step 2 — Animation description
    animation = generate_animation(script)
    print("\nANIMATION READY:\n", animation)

    # Step 3 — Voice generation
    voice = generate_voice(script)
    print("\nVOICE READY:\n", voice)

    # (NOTE: In real world you will render video here)
    fake_video_path = "output.mp4"

    # Step 4 — Upload to YouTube
    upload_to_youtube(
        video_path=fake_video_path,
        title="AI Animated Short",
        description=script
    )

    print("\nUPLOAD DONE!")

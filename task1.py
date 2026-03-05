good = True
if good:
    print(r"""           
           /|
        /\/ |/\
        \  ^   | /\  /\
  (\/\  / ^   /\/  )/^ )
   \  \/^ /\       ^  /
    )^       ^ \     (
   (   ^   ^      ^\  )
    \___\/____/______/
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |""")
else:
    print(r"""    
    [________________]
     |              |
     |     //\\     |
     |    <<()>>    |
     |     \\//     |
      \____________/
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |
          |    |""")
torch_lit = True
if torch_lit:
    outcome = ("Flicker: My torch is lit, now I have to find a way to get out of here.")
else:
    outcome = ("Doom: My torch isn't lit. I don't know what I'm going to do now!")
print(outcome)

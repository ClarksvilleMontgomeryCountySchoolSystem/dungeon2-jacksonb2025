bad = True
if bad:
    print(r"""         
         @\_______/@
        @|XXXXXXXX |
       @ |X||    X |
      @  |X||    X |
     @   |XXXXXXXX |
    @    |X||    X |             V
   @     |X||   .X |
  @      |X||.  .X |                      V
 @      |%XXXXXXXX%||
@       |X||  . . X||
        |X||   .. X||                               @     @
        |X||  .   X||                               ||====%
        |X|| .    X||                               ||    %
        |X||.     X||                               ||====%
       |XXXXXXXXXXXX||                              ||    %
       |XXXXXXXXXXXX||                              ||====% .
       |XX|        X||                              ||    %  .
       |XX|        X||                              ||====%   .
       |XX|        X||                              ||    %     .
       |XX|======= X||                              || .. %  ........
===== /            X||                              ||    %
                   X||                              ||    %
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
else:
    print(r"""         
         @\_______/@
        @|XXXXXXXX |
       @ |X||    X |
      @  |X||    X |
     @   |XXXXXXXX |
    @    |X||    X |             V
   @     |X||   .X |
  @      |X||.  .X |                      V
 @      |%XXXXXXXX%||
@       |X||  . . X||
        |X||   .. X||                               @     @
        |X||  .   X||.                              ||====%
        |X|| .    X|| .                             ||    %
        |X||.     X||   .                           ||====%
       |XXXXXXXXXXXX||     .                        ||    %
       |XXXXXXXXXXXX||         .                 .  ||====% .
       |XX|        X||                .        .    ||    %  .
       |XX|        X||                   .          ||====%   .
       |XX|        X||              .          .    ||    %     .
       |XX|======= X||============================+ || .. %  ........
===== /            X||                              ||    %
                   X||           /)                 ||    %
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
drawbridge_raised = True
if drawbridge_raised:
    outcome = ("Doom: Aw man I have to find another way now. I wonder how long this is going to take.")
else:
    outcome = ("Thunder: Yes I can finally get out! I'm finally free!")
print(outcome)
'''   
Topic: Flowchart of file and file mode.
 
            
                                            opening file
                                            -----------------
                                                    |
                                                    |
                                                    |
                                                    v
                            Reading            -------             Reading/writing
                        ---------------------- | for? |------------------------------------
                        |                      --------                                    |
                        |                           |                                      |
                        v                   writing |                                      |
                    ------                          |                                      |
                    |  r |               Yes        v                           Yes        v             NO
                    ------           ------------| Truncate?|                 ----------| Truncate?|-------------           
                                     |                |                       |                                  |
                                     |                | NO                    |                                  |
                                     |                |                       |                                  |
                                     v                v                       v                  --------------- v------------
                                    -----            ----                    ----                |   Begin              End   |        
                                    | w |            | a |                   |w+|                |                            |
                                    -----            -----                   ----               ----                         ----
                                                                                                | r+ |                       | a+ |
                                                                                                ----                         ------



'''
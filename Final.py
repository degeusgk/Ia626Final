#Final Project - IA626
# By Grace De Geus
#---------------------------------------------

import praw,json

reddit = praw.Reddit(client_id = 'hANTyPawYnpakQ', client_secret = 'mPssnqE6D4U_Jd04oxrEZ8UDAfk', username = 'Ia626_Final', password = 'Ia626_Final', user_agent = 'IA626')

subreddit = reddit.subreddit('coronavirus')

top_corona = subreddit.top('day')

Output_File = open("results.txt",mode="w", encoding="utf8")

'''
# Dictionary Format#
conversedict = {post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],

                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                                            
                post_id: [parent_content, {reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content],
                                            reply_id:[votes, reply_content]}],
                }
'''
post_number = 1
conversedict = {}
removal_reason_hist = {}
comment_number = 0
removed_number = 0
#Iterate through all posts in this subreddit
for submission in top_corona:
    Output_File.write("\n")
    Output_File.write(submission.title)
    Output_File.write("\n")
    #Load all comments
    submission.comments.replace_more(limit=None)
    #Iterate through all comments on this post
    for comment in submission.comments.list():
        #If we have not read this comment before
        if comment.id not in conversedict:
            #Add it to our dictionary for later
            conversedict[comment.id] = [comment.body,{}]
            #If this is not a top level comment
            if comment.parent() != submission.id:
                #Capture the higher level comment ID
                parent = str(comment.parent())
                #Populate the dictionary with the comment information
                conversedict[parent][1][comment.id] = [comment.created_utc, comment.body, comment.replies]
            #If this comment is a "removed by moderator" response
            if "removed" in comment.body and "* **" in comment.body:             
                #Capture the reason for comment removal
                removal_reason = comment.body.split("**")[1]
                #Add it to the histogram for later analysis
                if removal_reason not in removal_reason_hist:
                    removal_reason_hist[removal_reason] = 1
                else:
                    removal_reason_hist[removal_reason] += 1

        comment_number += 1
    
    if post_number % 10 == 0:
        break
    else :
        post_number += 1
        print("Still good...\n")

reply_number = 0
for post_id in conversedict:
    reply_number += 1
    message = conversedict[post_id][0]
    replies = conversedict[post_id][1]
    if len(replies) > 1:
        if "[removed]" in message:
            removed_number += 1
        for reply in replies:
            reply_number += 1
            body = replies[reply][1]
            if "[removed]" in replies[reply][1]:
                removed_number += 1
            if "removed" in body and "* **" in body:
                removal_reason = body.split("**")[1]
                if removal_reason not in removal_reason_hist:
                    removal_reason_hist[removal_reason] = 1
                else:
                    removal_reason_hist[removal_reason] += 1

#for reason in removal_reason_hist:
Output_File.write(json.dumps(removal_reason_hist))
   
print("Total Removed: " + str(removed_number) + "\n")
print("Total Comments: " + str(reply_number) + "\n")
print(removal_reason_hist)
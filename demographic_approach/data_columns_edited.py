# 1 = column is feature
# 1.5 = could be feature but might not be enough data
# 2 = column may be useful for coding
# 3 = column is useless
# 4 = column should be feature engineered into something useful

# Note regarding columns that are years/dates -- we probably shouldn't include them as absolute Years
# because that inhibits generality, but may be possible to engineer them into
# something useful -- e.g for ranges give size of range, or transform into years
# prior to nomination, or age when it occured
columns = [
    (1, "name", "Nominee’s Full Name", 3),
    (2, "yrnom", "Year of Nomination to the Court", 4),  # Not sure if should be included
    (3, "posit", "Nominated for Chief or Associate Justice", 1),
    (4, "recess", "Was this a Recess Appointment?", 1),
    (5, "success", "Did the Nominee Become a Justice or Chief Justice?", 3),
    (6, "id", "Unique Nomination Identification Number", 2),
    (7, "analu", "Unit of Analysis", 2),
    (8, "seatid", "Seat Identification Number", 3),
    (9, "spaethid", "Justice Identification Number Assigned by the U.S. Supreme Court Database", 2),
    (10, "zukid", "Identification Number Assigned by Z", 2),
    (13, "birthcit", "Nominee's Place of Birth", 1),#categorical
    (14, "birthst", "Nominee's Place of Birth", 3), #<- redundant
    (15, "childcit", "Nominee's Childhood Location", 3), #<- redundant/effectively equivalent
    (16, "childst", "Nominee's Childhood Location", 1),#categorical
    (17, "childsur", "Nominee's Childhood Surroundings", 1),#categorical
    (18, "famses", "Nominee's Family Economic Status", 1),#categorical
    (19, "fathpol", "Tradition of Judicial Service within Nominee's Family", 1),#categorical
    (19, "famjud", "Tradition of Judicial Service within Nominee's Family", 1),#categorical
    (20, "nomrelig", "Nominee's Religion", 1),#categorical
    (21, "natorig", "Nominee's Nation Origin", 1),#categorical
    (22, "race", "Nominee's Race/Ethnicity", 1),#categorical
    (23, "gender", "Nominee's gender", 1),
    (24, "mothname", "Name of Nominee's Mother", 3),
    (25, "fathname", "Name of Nominee's Father", 3),
    (26, "fathoccu", "Primary Occcupation of the Nominee's Father", 1),#categorical
    (29, "fathpoln", "Number of Political Offices Held by Nominee's Father", 1),
    (31, "undsch", "Name of Nominee's Undergraduate Institution", 4),#categorical
    (32, "undsta", "Nominee’s Undergraduate Status", 2),
    (33, "unddat", "Last Year at Undergraduate Institution", 4),
    (34, "undschn", "Number of Undergraduate Institutions Attended by Nominee", 1),
    (35, "gradsch", "Name of Nominee’s Graduate Institution", 1), #categorical
    (36, "gradsta", "Nominee’s Graduate Status", 1), #categorical
    (37, "graddat", "Last Year at Graduate Institution", 4),
    (38, "gradschn", "Number of Graduate Institutions Attended by Nominee", 1),
    (39, "lawsch", "Name of Nominee’s Law School", 1), #categorical
    (40, "lawsta", "Nominee’s Law School Status", 1), #categorical
    (41, "lawdat", "Nominee’s Last Year at Law School", 4),
    (42, "lawschn", "Number of Law Schools Attended by Nominee", 1),
    (43, "read", "Name of Mentor if Nominee Read the Law", 3),
    (44, "readst", "State Where Nominee Read the Law", 1),
    (45, "readyr", "Last Year Nominee Read the Law", 4),
    (46, "readn", "Number of Mentors if Nominee Read the Law", 4),
    (47, "marryn", "Number of Nominee’s Marriages", 1),
    (48, "spouse", "Name of Nominee’s Last Spouse", 3),
    (49, "marryr", "Year of Nominee’s Marriage to Last Spouse", 3),
    (50, "child", "Number of Nominee’s Children", 1),
    (51, "militbr", "Nominee’s Military Service—Branch", 1), #categorical
    (52, "milityrs", "Nominee’s Years of Military Service", 4),
    (54, "militran", "Nominee’s Highest Rank Attained in the Military", 3),
    (55, "militwar", "War During Which Nominee Served", 3),
    # Might be useful even if overfitted, also could engineer it by getting data
    # about the leanings of who they clerked for
    (56, "clerkj", "Name of U.S. Supreme Court Justice for Whom Nominee Clerked", 4), #categorical
    (57, "clerkyrs", "Years of Nominee’s Clerkship with a U.S. Supreme Court Justice", 4),
    (59, "barst1", "First State in which Nominee was Admitted to the Bar", 1.5),
    (60, "baryr1", "Nominee’s Year of Admission to the First State Bar", 4),
    # definitely not enough data for these two
    (61, "barst2", "Second State in which Nominee was Admitted to the Bar", 3),
    (62, "baryr2", "Nominee’s Year of Admission to the Second State Bar", 3),
    (63, "barst3", "Third State in which Nominee was Admitted to the Bar", 3),
    (64, "baryr3", "Nominee’s Year of Admission to the Third State Bar", 3),
    (65, "privtyp1", "Type of Nominee’s First Private Law Practice", 1.5),#categorical
    (66, "privst1", "State of Nominee’s First Private Law Practice", 1.5),
    (67, "privyrs1", "Years of Nominee’s First Private Law Practice", 4),
    (69, "privtyp2", "Type of Nominee’s Last Private Law Practice", 1.5),#categorical
    (70, "privst2", "State of Nominee’s Last Private Law Practice", 1.5),
    (71, "privyrs2", "Years of Nominee’s Last Private Law Practice", 4),
    # overfit
    (73, "schname1", "Name of First Law School in which Nominee Taught", 1.5),#categorical
    (74, "schrank1", "Title at First Law School in which Nominee Taught", 1.5),#categorical
    (75, "schyrs1", "Years at First Law School in which Nominee Taught", 4),
    (77, "schname2", "Name of Last Law School in which Nominee Taught", 1.5), #categorical
    (78, "schrank2", "Title at Last Law School in which Nominee Taught", 1.5), #categorical
    (79, "schyrs2", "Years at Last Law School in which Nominee Taught", 4),

    (81, "schn", "Number of Law Schools in which Nominee Taught", 1.5),
    # definitely not helpful
    (82, "schcon", "Nominee Taught at Same Law School During Non-Consecutive Periods", 3),
    (83, "sttrist", "State in which Nominee Served as State Trial Court Judge", 1),
    (84, "sttriyrs", "Years Nominee Served as a State Trial Court Judge", 4),
    (86, "stapst", "State in which Nominee Served as a State Intermediate Appellate Court Judge", 1),
    (87, "stapyrs", "Years Nominee Served as a State Intermediate Appellate Court Judge", 4),
    (89, "stsupst", "State in which Nominee Served as a Justice on State’s Highest Court", 1),
    (90, "stsupyrs", "Years Nominee Served as a Justice on State’s Highest Court", 4),
    (92, "feddist", "State in which Nominee Served as a U.S. District Court Judge", 1),
    (93, "feddi", "District in which Nominee Served as a U.S. District Court Judge", 3),
    (94, "feddiyrs", "Years Nominee Served as a U.S. District Court Judge", 4),
    (96, "fedca", "U. S. Court of Appeals on which Nominee Served", 1),
    (97, "fedcayrs", "Years Nominee Served as a U.S. Court of Appeals Judge", 4),
    (99, "usasat", "District in which Nominee Served as an Assistant U.S. Attorney", 1.5),
    (100, "usasatyrs", "Years Nominee Served as an Assistant U.S. Attorney", 4),
    (102, "usat", "District in which Nominee Served as a U.S. Attorney", 1.5),
    (103, "usatyrs", "Years Nominee Served as a U.S. Attorney", 4),
    (105, "ussgoyrs", "Years Nominee Served in the Office of the U.S. Solicitor General", 4),
    (107, "ussgyrs", "Years Nominee Served as the U.S. Solicitor General", 4),
    (109, "usagoyrs", "Years Nominee Served in the Office of the U.S. Attorney General", 4),
    (111, "usagyrs", "Years Nominee Served as the U.S. Attorney General", 4),
    (113, "uscab", "Name of U.S. Cabinet in which Nominee Served at a Level Below Secretary (Other than justice)", 1.5), #categorical
    (114, "uscabyrs", "Years Nominee Served in the U.S. Cabinet at a Level Below Secretary", 1.5),
    (116, "ussec", "Name of U.S. Cabinet Department in which the Nominee served at the Secretary Level", 1.5),#categorical
    (117, "ussecyrs", "Years Nominee Served in the U.S. Cabinet at the Secretary Level", 4),
    (119, "usage", "Name of Executive Commission, Agency, or White House Post in which the Nominee Served at a level below head", 1.5),#categorical
    (120, "usageyrs", "Years Nominee Served on an Executive Commission, Agency, or in a White House Post at a level below head", 1.5),
    (122, "usagh", "Name of Executive Commission or Agency that Nominee Headed", 1.5),#categorical
    (123, "usaghyrs", "Years Nominee Served as Head of an Executive Agency or Commission", 1.5),
    (125, "uspresyrs", "Years Nominee Served as President of the United States", 3),
    (127, "ushr1", "State Nominee Represented in the U.S. House of Representatives (First Service)", 1.5),#categorical
    (128, "ushryrs1", "Years Nominee Served in the U.S. House of Representatives (First Service)", 4),
    (130, "ushr2", "State Nominee Represented in the U.S. House of Representatives (Second Service)", 1.5),#categorical
    (131, "ushryrs2", "Years Nominee Served in the U.S. House of Representatives (Second Service)", 1.5),
    (133, "ussn1", "State Nominee Represented in the U.S. Senate (First Service)", 1.5),#categorical
    (134, "ussnyrs1", "Years Nominee Served in the U.S. Senate (First Service)", 4),
    (136, "ussn2", "State Nominee Represented in the U.S. Senate (Second Service)", 1.5),#categorical
    (137, "ussnyrs2", "Years Nominee Served in the U.S. Senate (Second Service)", 4),
    (139, "conconv", "Was Nominee a Delegate to the 1787 Constitutional Convention?", 3),
    (140, "concong", "State Nominee Represented in the Continental Congress", 3),
    (141, "concongyrs", "Years Nominee Served in the Continental Congress", 3),
    (143, "artcon", "State Nominee Represented in the Congress under the Articles of Confederation", 3),
    (144, "artconyrs", "Years Nominee Served in the Congress under the Articles of Confederation", 3),
    (146, "artconsp", "Nominee Served Two Separate Terms in the Congress under the Articles of Confederation", 3),
    # might be overfitted, but just make a binary deputy/city/attorney feature
    (147, "citat", "City and State in which Nominee Served as a Deputy or City Attorney", 4),
    (148, "citatyrs", "Years Nominee Served as a Deputy or City Attorney", 4),
    (150, "cdep", "State in which Nominee Served as an Assistant District or County Attorney", 1.5),
    (151, "cdepyrs", "Years Nominee Served as an Assistant District or County Attorney", 4),
    (153, "cdis", "State in which Nominee Served as a District or County Attorney", 1.5),
    (154, "cdisyrs", "Years Nominee Served as the District or County Attorney", 4),
    (156, "saag", "State in which Nominee Served as a State Assistant Attorney General", 1.5),
    (157, "saagyrs", "Years Nominee Served as a State Assistant Attorney General", 4),
    (159, "stag", "State in which Nominee Served as State Attorney General", 1.5),
    (160, "stagyrs", "Years Nominee Served as State Attorney General", 4),
    (162, "ltgov", "State in which Nominee Served as Lt. Governor", 1.5),
    (163, "ltgov1", "First Year Nominee Served as Lt. Governor", 3),
    (164, "ltgov2", "Last Year State Nominee Served as Lt. Governor", 3),
    (163, "ltgovyrs", "Years Nominee Served as Lt. Governor", 4),
    (165, "gov", "State in which Nominee Served as Governor", 1.5),
    (166, "govyrs", "Years Nominee Served as Governor", 4),
    (168, "stcab", "State in which Nominee Served on a State Cabinet", 1.5),
    (169, "stcabyrs", "Years Nominee Served on a State Cabinet", 4),
    (171, "mayor", "City and State in which Nominee Served as Mayor", 1.5),
    (172, "mayoryrs", "Years Nominee Served as Mayor", 4),
    (174, "stsenate", "State in which Nominee Served in the State Senate", 1.5),
    (175, "stsenyrs", "Years Nominee Served in State Senate", 4),
    (177, "sthouse", "State in which Nominee Served in the State House", 1.5),
    (178, "sthseyrs", "Years Nominee Served in State House", 4),
    (180, "ctycl", "City and State in which Nominee Served on the City Council", 1.5),
    (181, "ctyclyrs", "Years Nominee Served on the City Council", 4),
    (183, "commsn", "State Commission/Convention on which Nominee Served", 1.5),
    (184, "commsnyrs", "Years Nominee Served on a State Commission", 4),
    (186, "datenom", "Date of Nomination (or Recess Appointment) to the Court", 1), #need to normalize WRT nomination year
    (187, "datesen", "Date Nomination Received in the Senate", 3), #<- redundant WRT yrnom
    (188, "judnom", "Nominee a Judge at Time of Nomination (or Recess Appointment)", 1),
    (189, "usjnom", "Nominee a Federal Judge at Time of Nomination (or Recess Appointment)", 1),
    (190, "stjnom", "Nominee a State Judge at Time of Nomination (or Recess Appointment)", 1),
    (191, "prsznom", "Nominee in Private Practice at Time of Nomination (or Recess Appointment)", 1),
    (192, "prstnom", "Nominee in Private Practice at Time of Nomination (or Recess Appointment)", 1),
    (193, "prposnom", "Nominee a Legal Academic at Time of Nomination (or Recess Appointment)", 1),
    (194, "prschnom", "Legal Academic at Time of Nomination (or Recess Appointment)", 1),
    (195, "govatnom", "Working in a Legal Position for the U.S. Government at Time of Nomination (or Recess Appointment", 1),
    (196, "uslenom", "Federal Legislator at Time of Nomination (or Recess Appointment)", 1),
    (197, "uslesnom", "Federal Legislator at Time of Nomination (or Recess Appointment)", 1),
    (198, "stlenom", "State Legislator at Time of Nomination (or Recess Appointment)", 1),
    (199, "stlesnom", "State Legislator at Time of Nomination (or Recess Appointment)", 1),
    (200, "stexpnom", "Governor or other Executive Position in State Government at Time of Nomination", 1),
    (201, "govnom", "Governor or Other Executive Position in State Government at Time of Nomination", 1),
    (202, "usexnom", "(Non-Legal) Position in the U.S. Executive Branch at Time of Nomination (or Rece", 1),
    (203, "yrposnom", "Number of Years in Position Held at Time of Nomination (or Recess Appointment)", 1),
    (204, "agenom", "Age at Time of Nomination (or Recess Appointment)", 1),
    (205, "stnom", "Official Home State of Nomination (or Recess Appointment)", 1), #categorical
    (206, "parnom", "Political Party Affiliation at Time of Nomination (or Recess Appointment)", 1),#categorical
    (207, "prparnom", "Previous Party Affiliations of Nominee", 1),#categorical
    (208, "prdssr", "Name of Justice Nominee (or Recess Appointee) is Replacing", 3),
    (209, "presname", "Name of the Nominating President (or Appointing President, in the Case of a Recess", 3),
    (210, "prespart", "Political Party Affiliation of the Nominating President (or Appointing President, in the", 1),#categorical
    (211, "nompres", "NOMINATE Ideology Score of the Nominating President (or Appointing President, in", 1),
    (212, "socpres", "Social Liberalism Score of the Nominating President (or Appointing President, in the", 1),
    (213, "econpres", "Economic Liberalism Score of the Nominating President (or Appointing President, in", 1),
    (214, "congress", "Congress Number at the Time of Nomination (or Recess Appointment)", 3),
    (215, "senparty", "Dominant Political Party of the U.S. Senate at the Time of Nomination (or Recess Appointment)", 1),#categorical
    (216, "nomsen", "NOMINATE Ideology Score of the Score of the Median Member of the U.S. Senate at", 1),
    (217, "ideo", "Segal & Cover Score of the Nominee’s Ideology", 1),
    (218, "mednmq1", "Name of Martin & Quinn’s Most Likely Median in Term Prior to Nomination (or Re", 1),
    (219, "medmq1", "Martin & Quinn’s Median in Term Prior to the Nomination (or Recess Appointment)", 3),
    (220, "mednmq2", "Name of Martin & Quinn’s Most Likely Median in the Term of Nomination (or Re", 3),
    (221, "medmq2", "Martin & Quinn’s Median in Term of Nomination (or Recess Appointment)", 3),
    (222, "qual", "Segal & Cover Score of Nominee’s Qualifications", 3),
    (223, "abarate", "ABA Committee on the Federal Judiciary Rating of Nominee", 1),
    (224, "abavote", "Vote of the ABA’s Committee on the Federal Judiciary on the Nominee", 3),
    (225, "heardate", "First Date of Judiciary Committee Public Hearings on the Nominee", 3),
    (226, "heardays", "Total Number of Days of Judiciary Committee Public Hearings on the Nominee", 3),
    (227, "comdvote", "Date of the Final Vote of the Judiciary Committee on the Nominee", 3),
    (228, "comvote", "Final Vote of the Judiciary Committee on the Nominee", 3),
    (229, "intpro", "Number of Interest Groups Supporting the Nominee", 3),
    (230, "intanti", "Number of Interest Groups Opposing the Nominee", 3),
    (231, "sendate", "Date of Final Action on the Nominee by the Senate", 3),
    (232, "senact", "Final Action on the Nominee by the Senate", 3),
    (233, "sensupp", "Number of Senate Votes in Favor of the Nominee on Final Action", 3),
    (234, "senopp", "Number of Senate Votes Against the Nominee on Final Action", 3),
    (235, "serve", "Did the Nominee Serve on the Court?", 3),
    (236, "withdraw", "Date of Withdrawal of the Nomination", 3),
    (237, "dateserb", "Date Judicial Oath Taken by the Nominee", 3),
    (238, "datesere", "Date Justice’s Service on the Court Terminated", 3),
    (239, "agedep", "Justice’s Age at Time of Departure from the Court", 3),
    (240, "reasdep", "Justice’s Reason for Departure from the Court", 3),
    (241, "postdep", "Type of Position Held by Justice Immediately After Departure from the Court", 3),
    (242, "scssr", "Name of Justice Who Replaced Departing Justice", 3),
    (243, "deathd", "Date of Death", 3),
    (244, "deathcit", "Place of Death", 3),
    (245, "deathst", "Place of Death", 3),
    (246, "deathag", "Age at Time of Death", 3),
]

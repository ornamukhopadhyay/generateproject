import random
from flask import Flask, render_template

#integration into a website would take too long, could not do it right now


print(
    "Learn more about science and maths! Answers: Science, Mathematics! Pick a subject." )
enter1 = input()
enter1 = enter1.lower(
)  #this makes everything lowercase so it won't be case sensitive
if enter1 == "science":
    enter2 = input(
        "What specific subject would you like to know about? Answers: Physics, Biology, Chemistry, Computer Science. "
    )
    enter2 = enter2.lower()
    if enter2 == "physics":
        enter3 = input(
            "Cool! Which field of physics? Answer: Classical Mechanics, Modern Physics "
        )
        enter3 = enter3.lower()
        if enter3 == "classical mechanics":
            print("Awesome! Here are some research project ideas. ")
            links = {1:"https://wp.stolaf.edu/physics/student-special-projects/fall-2014-classical-mechanics-phys-374-final-projects/", 2:"https://arxiv.org/pdf/1001.0131.pdf", 3:"https://ocw.mit.edu/courses/physics/8-223-classical-mechanics-ii-january-iap-2017/projects/", 4:"https://www.juliantrubin.com/fairprojects/physics/mechanics.html", 5:"https://sites.google.com/site/mcmurryphysicsdepartment/projects-research/class-projects"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "modern physics":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.monash.edu/science/schools/physics/undergraduate/research/example-honours-projects", 2:"https://physics.anu.edu.au/study/projects/project.php?ProjectID=141",3:"https://physics.dartmouth.edu/research/all-projects",4:"https://www.phywe.com/en/physics/university/thermodynamics/",5:"https://smp.uq.edu.au/research/projects/condensed-matter-physics"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    elif enter2 == "biology":
        enter3 = input(
            "Cool! Which field of biology? Answer: Botany, Zoology, Microbiology, Anatomy, Molecular Bio, Evolutionary Bio? "
        )
        enter3 = enter3.lower()
        if enter3 == "botany":
            print("Awesome! Here are some research project ideas.")
            links = {1: "https://www.1000sciencefairprojects.com/Plant-Biology/Botany-Projects-for-College-Students.php",2:"https://www.juliantrubin.com/plantprojects.html",3:"https://www.juliantrubin.com/encyclopedia/topics/botany.html",4:"http://www.kidsprojects.info/Plant-Biology/Botany-Projects-for-Degree-Students.php",5:"https://www.findaphd.com/phds/phd-research-projects/botany-plant-science/?22gc210"}
            choice = random.choice(list(links.values()))
            print(choice)
            
        elif enter3 == "zoology":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.zoo.cam.ac.uk/research/groups/insect-neuro/research-projects", 2:"https://www.juliantrubin.com/zoologyprojects.html", 3:"https://nsufl.libguides.com/biol3300/project", 4:"http://www.sapub.org/journal/articles.aspx?journalid=1093", 5:"https://academic.oup.com/cz"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "microbiology":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.nature.com/articles/s41467-020-18168-3", 2:"https://www.nature.com/articles/s41467-020-18108-1", 3:"https://www.sciencedaily.com/releases/2020/08/200827141245.htm", 4:"https://www.sciencedaily.com/releases/2020/08/200827141250.htm", 5:"https://www.sciencedaily.com/releases/2020/08/200827155006.htm"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "anatomy":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5380403/", 2:"https://www.news-medical.net/news/20200820/Scientists-investigate-the-role-of-contractility-and-microbiota-in-chronic-constipation.aspx", 3:"https://www.longdom.org/open-access/vascular-system-in-long-bone-is-far-from-well-known.pdf", 4:"https://www.longdom.org/open-access/estro-oxygen-of-bosomvirulent-growth-after-menopause.pdf", 5:"https://www.longdom.org/open-access/is-saliva-an-alternative-noninvasive-sample-for-the-estimation-of-protein-profile-amongst-diabetics-and-genderbased-diagnostics-2161-0940-1000255.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "molecular bio":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.nature.com/articles/s41597-020-00623-x", 2:"https://www.nature.com/articles/s41467-020-18222-0", 3:"https://www.lsuhs.edu/departments/school-of-graduate-studies/biochemistry-and-molecular-biology/research", 4:"https://pubmed.ncbi.nlm.nih.gov/32856411/", 5:"https://biochemistry.med.uky.edu/potential-projects"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "evolutionary bio":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.juliantrubin.com/topicprojects/evolutionprojects.html", 2:"https://www.biology.lu.se/research/research-groups/theoretical-population-ecology-and-evolution-group/research-projects", 3:"https://www.evolbio.mpg.de/3024391/open-projects-2020", 4:"https://bmcevolbiol.biomedcentral.com/articles", 5:"https://www.scientificamerican.com/evolutionary-biology/"}
            choice = random.choice(list(links.values()))
            print(choice)
   
        else:
            print("I'm sorry; please try again.")

    elif enter2 == "chemistry":
        enter3 = input(
            "Cool! Which field of Chemistry? Answer: Organic, Inorganic, Physical, Analytical, Biochemistry? ")
        enter3 = enter3.lower()
        if enter3 == "organic":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.1000sciencefairprojects.com/Chemistry/Organic-Chemistry-Project-Ideas.php", 2:"https://www.findaphd.com/phds/phd-research-projects/organic-chemistry/?22g8710", 3:"https://uniprojects.net/projects/organic-chemistry-project-topics-materials/", 4:"https://www.seminarsonly.com/Engineering-Projects/Chemistry/Organic-Chemistry-Project-Experiments-Topics.php", 5:"https://www.youtube.com/watch?v=PmvLB5dIEp8"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "inorganic":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.youtube.com/watch?v=OUj4j6td1es", 2:"https://uniprojects.net/projects/inorganic-chemistry-project-topics-materials/", 3:"https://www.acs.org/content/acs/en/careers/college-to-career/areas-of-chemistry/inorganic-chemistry.html", 4:"https://www.chemistryworld.com/inorganic-chemistry/183.subject", 5:"https://www.findaphd.com/phds/phd-research-projects/inorganic-chemistry/?22gY610"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "physical":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.evansville.edu/majors/chemistry/research.cfm", 2:"https://www.seminarsonly.com/Engineering-Projects/Chemistry/Physical-Chemistry-Projects-Experiments.php", 3:"https://www.scienceshopusa.com/pages/physical-science-projects", 4:"https://www.chem.ucsb.edu/research/physical", 5:"https://www.juliantrubin.com/chemistryprojects.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "analytical":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://afribary.com/works/fields/natural-applied-sciences/sub-fields/analytical-chemistry", 2:"https://www.acs.org/content/acs/en/education/students/highschool/chemistryclubs/activities/simulations.html", 3:"https://www.leybold-shop.com/chemistry/catalogue-of-experiments-chemistry/analytical-chemistry.html", 4:"https://www.leybold-shop.com/chemistry/catalogue-of-experiments-chemistry/analytical-chemistry.html", 5:"https://www.youtube.com/watch?v=AO67MnZaAvQ"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "biochemistry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"http://www.all-science-fair-projects.com/category98.html", 2:"https://www.juliantrubin.com/fairprojects/biochemistry/medical_biochemistry.html", 3:"https://www.youtube.com/watch?v=3vy__KvTi6I&list=PL9jo2wQj1WCNYMXKLWy22FWxH_Yvxev_y", 4:"https://www.iprojectmaster.com/final-year-projects-materials/BIOCHEMISTRY", 5:"https://www.sciencedaily.com/releases/2020/08/200828140310.htm"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    elif enter2 == "computer science":
        enter3 = input(
            "Alright, what field? Answers: Theoretical, Computer Engineering, Applications "
        )
        enter3 = enter3.lower()
        if enter3 == "theoretical":
            print("Awesome! Here are some project ideas!")
            links = {1:"https://arxiv.org/abs/2008.12235", 2:"https://arxiv.org/abs/2008.12224", 3:"https://www.youtube.com/watch?v=aircAruvnKk&t=1s", 4:"https://arxiv.org/abs/2008.12151", 5:"https://arxiv.org/abs/2008.12229"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "computer engineering":
            print("Awesome! Here are some research project ideas!")
            links = {1:"https://www.1000sciencefairprojects.com/Software-Projects/Software-Project-Ideas-High-School-Students.php", 2:"https://pdos.csail.mit.edu/", 3:"https://www.youtube.com/watch?v=O753uuutqH8", 4:"http://projects.csail.mit.edu/pl/", 5:"https://blogs.uw.edu/ajko/2015/10/05/the-black-hole-of-software-engineering-research/"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "applications":
            print("Awesome! Here are some research project ideas!")
            links = {1:"https://arxiv.org/abs/1612.03144", 2:"https://arxiv.org/abs/2008.09094", 3:"https://arxiv.org/abs/2008.12190", 4:"https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN", 5:"https://www.geeksforgeeks.org/computer-science-projects/"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    else:
        print("I'm sorry; please try again.")

elif enter1 == "mathematics":
    enter2 = input(
        "What specific subject would you like to know about? Answers: Geometry, Trigonometry, Calculus, Algebra, Statistics. "
    )
    enter2 = enter2.lower()
    if enter2 == "geometry":
        enter3 = input(
            "Cool! Which field of Geometry? Answer: Euclidian Geometry, Analytical Geometry,Projective geometry, Differential geometry, Non-Euclidean geometry, Topology. ")
        enter3 = enter3.lower()
        if enter3 == "euclidean geometry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://pdfs.semanticscholar.org/e83c/ccd789d50e13c0252666e726d390b7aabef6.pdf", 2:"https://www.math.colostate.edu/~pries/470/470HW06/470pj06.html", 3:"https://www.uib.no/en/rg/algebraisk-geometri/54048/euclidean-and-non-euclidean-geometry", 4:"https://www.sciencebuddies.org/science-fair-projects/project-ideas/Math_p011/pure-mathematics/chain-reaction-inversion-pappus-chain-theorem?fave=yes&amp%3Bisb=cmlkOjEwMTY5NSxzaWQ6MTA4LHA6MQ&amp%3Bfrom=TSW", 5:"https://faculty.math.illinois.edu/~mjunge/40216/Hvidsten.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "analytical geometry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://faculty.math.illinois.edu/~mjunge/40216/Hvidsten.pdf", 2:"https://demonstrations.wolfram.com/topic.html?topic=Analytic+Geometry&limit=20", 3:"https://www.youtube.com/watch?v=1Mg97CoaWwg", 4:"https://encyclopedia2.thefreedictionary.com/analytical+geometry",5:"https://www.juliantrubin.com/fairprojects/mathematics/geometry.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "projective geometry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://demonstrations.wolfram.com/topic.html?topic=projective+geometry&limit=20", 2:"https://mste.illinois.edu/dildine/classes/ci499fall04/final.doc", 3:"https://www.h-its.org/projects/projective-geometry-transformations-of-four-flags/", 4:"https://www.youtube.com/watch?v=qlAgviCoJv0", 5:"http://www.maths.dur.ac.uk/users/anna.felikson/Projects/projective/proj.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "differential geometry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"http://theronhitchman.github.io/differential-geometry/projects/", 2:"http://www.pitt.edu/~jdeblois/final_topics.pdf", 3:"https://www2.mathematik.hu-berlin.de/~diffgeo/en/index.php?seite=projekte", 4:"https://math.berkeley.edu/wp/drp/project-ideas/", 5:"https://www.mi.fu-berlin.de/en/math/groups/ag-geom/projects/projects/index.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "non-euclidean geometry":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://faculty.math.illinois.edu/~mjunge/40216/Hvidsten.pdf", 2:"http://faculty.gordonstate.edu/gclement/Math3301/NonEuclidean%20Geometries_Project.pdf", 3:"http://www.science4all.org/article/non-euclidean-geometry-and-map-making/", 4:"https://mathstat.slu.edu/escher/index.php/Non-Euclidean_Art_Project", 5:"https://www.pitt.edu/~jdnorton/teaching/HPS_0410/chapters/non_Euclid_construction/index.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "topology":
            print("Awesome! Here are some research project ideas.")
            links = {1:"http://homepage.math.uiowa.edu/~idarcy/AT/project.html", 2:"http://topology.eecs.umich.edu/", 3:"https://www.youtube.com/watch?v=nI4j_IE87Xo", 4:"https://www.sciencebuddies.org/science-fair-projects/project-ideas/Math_p030/pure-mathematics/topologies", 5:"https://www.juliantrubin.com/fairprojects/mathematics/miscellany.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        else: 
            print("I'm sorry; please try again.")
    elif enter2 == "trigonometry":
        enter3 = input(
            "Cool! Which field of Trigonometry? Answer: Core, Plane, Spherical, Analytical? "
        )
        enter3 = enter3.lower()
        if enter3 == "plane":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.mathalino.com/reviewer/plane-trigonometry", 2:"http://fs.unm.edu/ProblemsGeomTrig-en.pdf", 3:"https://quod.lib.umich.edu/u/umhistmath/ABN8205.0001.001?rgn=main;view=fulltext", 4:"https://www.cemc.uwaterloo.ca/contests/euclid_eWorkshop/eew_ps4.pdf", 5:"https://www.math.txstate.edu/resources-student/mathcats/course/1317.html"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "core":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.khanacademy.org/commoncore/grade-HSF-F-TF", 2:"https://www.varsitytutors.com/trigonometry-practice-tests"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "spherical":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://mathworld.wolfram.com/SphericalTrigonometry.html", 2:"https://www.youtube.com/watch?v=hcXbLRPq5vc&list=PLSFxG38qlzCmZ7BrhnEE5I5ZeQdGwdMdm&index=87", 3:"https://www.math.stonybrook.edu/~tony/archive/hon101s08/spher-trig.html", 4:"https://kpknudson.com/blog/2013/11/27/spherical-trigonometry", 5:"http://jwilson.coe.uga.edu/EMAT6680Fa2013/Lively/Spherical%20Triangles/Solving_Spherical_Triangles.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "analytical":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.profrobbob.com/pre-calculus/analytic-trigonometry-and-trig-proofs", 2:"https://www.slcc.edu/math/docs/oer-trigonometry.pdf", 3:"https://www.ck12.org/book/ck-12-college-precalculus/section/8.7/", 4:"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2695326/", 5:"https://hal.archives-ouvertes.fr/hal-01337947/document"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    elif enter2 == "calculus":
        enter3 = input(
            "Cool! Which field of calculus? Answer: Differential, Integral? ")
        enter3 = enter3.lower()
        if enter3 == "differential":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.youtube.com/watch?v=p_di4Zn4wz4", 2:"https://www.youtube.com/watch?v=SfruceeKV54", 3:"https://www.tandfonline.com/doi/abs/10.1080/10511979308965684", 4:"https://iopscience.iop.org/article/10.1088/1742-6596/1381/1/012003/pdf", 5:"https://faculty.ung.edu/jallagan/Courses%20materials/Math%201450%20Calculus%201/Syllabus%20and%20ebook/problems%20and%20solutions%20for%20calculus%201.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "integral":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.youtube.com/watch?v=6WUjbJEeJwM", 2:"https://www.youtube.com/watch?v=rfG8ce4nNh0", 3:"https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/unit-3-the-definite-integral-and-its-applications/part-a-definition-of-the-definite-integral-and-first-fundamental-theorem/problem-set-6/MIT18_01SC_pset3sol.pdf", 4:"https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf", 5:"http://web.archive.org/web/20031209102402/http://www.its.caltech.edu/~mamikon/VisCal.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    elif enter2 == "algebra":
        enter3 = input(
            "Cool! Which field of algebra? Answer: Advanced Algebra, Abstract Algebra, Linear Algebra, and Commutative Algebra "
        )
        enter3 = enter3.lower()
        if enter3 == "advanced algebra":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.math.stonybrook.edu/~aknapp/download/a2-alg-inside.pdf", 2:"https://rl.talis.com/3/surrey/lists/AAABE31E-4352-B727-DCA2-4CEC94FF98CE.html?lang=en-US", 3:"https://www.youtube.com/watch?v=ouUaxWVJNSI", 4:"https://www.edx.org/course/college-algebra-and-problem-solving", 5:"https://www.maa.org/math-competitions/putnam-competition"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "abstract algebra":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://math.dartmouth.edu/~jvoight/Sp2008-252/252-PROJ-topics.pdf", 2:"http://www.maths.gla.ac.uk/research/groups/algebra/", 3:"https://warwick.ac.uk/fac/sci/maths/undergrad/ughandbook/lecturers2016/ma469r/topics/2016topics/"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "linear algebra":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://www.youtube.com/watch?v=fNk_zzaMoSs&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", 2:"https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/", 3:"http://web.mit.edu/18.06/www/psets.shtml", 4:"https://www.sciencedirect.com/science/article/pii/0024379594905126", 5:"https://onlinelibrary.wiley.com/journal/10991506"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "commutative algebra":
            print("Awesome! Here are some research project ideas.")
            links = {1:"https://arxiv.org/pdf/1605.04832.pdf", 2:"https://faculty.math.illinois.edu/~r-ash/ComAlg.html", 3:"https://stacks.math.columbia.edu/download/algebra.pdf", 4:"https://link.springer.com/article/10.1007/s00283-018-9826-2", 5:"http://www1.spms.ntu.edu.sg/~frederique/chap2.pdf"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")
    elif enter2 == "statistics":
        enter3 = input(
            "Cool! Which field of statistics and probability? Answer: Descriptive Statistics and Inferential Statistics? "
        )
        enter3 = enter3.lower()
        if enter3 == "descriptive statistics":
            print("Awesome! Here are some research topics.")
            links = {1:"https://www.youtube.com/watch?v=QoQbR4lVLrs", 2:"https://mymission.lamission.edu/userdata/ngohp/docs/Math%20227%20Project%201%20Data%20Collection%20and%20Descriptive%20Statistics_Fall%202019.pdf", 3:"", 4:"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6350423/", 5:"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2770212/"}
            choice = random.choice(list(links.values()))
            print(choice)
        elif enter3 == "intferential statistics":
            print("Awesome! Here are some research topics.")
            links = {1:"https://www.youtube.com/watch?v=JyPIm-vxIKs&list=PLAwxTw4SYaPnVUrK_vL3r9tP6kuwAEzgQ", 2:"https://statisticsbyjim.com/basics/descriptive-inferential-statistics/", 3:"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5037948/", 4:"http://vassarstats.net/textbook/", 5:"https://scripts.iucr.org/cgi-bin/paper?cg5145"}
            choice = random.choice(list(links.values()))
            print(choice)
        else:
            print("I'm sorry; please try again.")

    else:
        print("I'm sorry; please try again.")
else:
    print("I'm sorry; please try again.")

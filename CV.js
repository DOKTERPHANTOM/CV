<script src="CV.js"></script>

document.addEventListener("DOMContentLoaded", function () {
  const hero = document.getElementById("hero");
  if (hero) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
        }
      });
    }, { threshold: 0.5 });

    observer.observe(hero);
  }
  console.log("JS loaded and working!");
});

   <h2>I am a young enthusiastic technology study looking to get my feet wet. Here is a little bit of
        infor about me, I am a 20 year old aspiring IT professional with a focus on Networking, Cybersecurity, 
        and Creative Problem Solving. I am currently pursuing a degree in Information Technology at Edovs, 
        where I am honing my skills in various IT domains. I have done larnt a lot of different coding languages,
        including Python, C#, and C++. I am passionate about using technology to solve real-world problems. I
        have also been introduced to cisco packet tracer, linux and aws cloud computing. I am always eager to learn
        new things and take on new challenges. I am excited to see where my journey in the IT field will take me.
        Feel free to explore my projects on my GitHub or contact me for any inquiries or collaborations. Other
        than that, I am a very friendly person and I am always willing to help out where I can. I am enjoy working 
        people and learning from them. I am also creative and enjoy using the english language to express myself.
        I am looking forward to working with you and learning from you. Thank you for taking the time to read my cover page.
    </h2>
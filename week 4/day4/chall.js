// ✅ Class Definition
class Video {
    constructor(title, uploader, time) {
      this.title = title;
      this.uploader = uploader;
      this.time = time;
    }
  
    watch() {
      console.log(`${this.uploader} watched all ${this.time} seconds of "${this.title}"!`);
    }
  }
  
  
  const video1 = new Video("Learn JavaScript in 1 Hour", "Alice", 3600);
  video1.watch();
  
  const video2 = new Video("Cute Cats Compilation", "Bob", 600);
  video2.watch(); 
  
 
  const videoData = [
    { title: "Understanding Async/Await", uploader: "DevJohn", time: 900 },
    { title: "Top 10 Coding Tips", uploader: "CodeGirl", time: 720 },
    { title: "How to Center a Div", uploader: "CSSMaster", time: 180 },
    { title: "React Crash Course", uploader: "FrontendGuru", time: 2400 },
    { title: "Intro to Cybersecurity", uploader: "TechSecure", time: 1500 }
  ];
  
 
  console.log("\n--- Batch Video Watch Log ---");
  const videoInstances = videoData.map(video => new Video(video.title, video.uploader, video.time));
  videoInstances.forEach(video => video.watch());
  
const { createApp } = Vue;

createApp({
  data() {
    return {
      expanded: false // starts collapsed
    };
  }
}).mount("#app");

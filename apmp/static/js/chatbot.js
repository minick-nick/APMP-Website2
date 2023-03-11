!(function () {
    let e = document.createElement("script"),
      t = document.head || document.getElementsByTagName("head")[0];
    (e.src =
      "https://cdn.jsdelivr.net/npm/rasa-webchat@1.x.x/lib/index.js"),
      // Replace 1.x.x with the version that you want
      (e.async = !0),
      (e.onload = () => {
        window.WebChat.default(
          {
            title: 'Paul',
            profileAvatar: "./static/images/icon/chatbot.png",
            subtitle: 'Apostle Paul Memorial Park Chatbot',
            showMessageDate: false,
            initPayload: '/welcome_msg',
            customData: { language: "en" },
            //"https://rasa-minicknick.cloud.okteto.net/"
            socketUrl: "http://localhost:8080",
          },
          null
        );
      }),
      t.insertBefore(e, t.firstChild);
      localStorage.clear();
})();
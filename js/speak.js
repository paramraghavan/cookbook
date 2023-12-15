function speak(text) {
    var voice = new SpeechSynthesisUtterance();
    voice.text = text;
    speechSynthesis.speak(voice);
}
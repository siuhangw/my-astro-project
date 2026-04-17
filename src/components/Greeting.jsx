import { useState } from 'preact/hooks';

export default function Greeting({messages}) {

  const [greeting, setGreeting] = useState(messages[0]);

  const randomMessage = () => {
    let newMessage = greeting;
    if (messages.length > 1) {
      while (newMessage === greeting) {
        const array = new Uint32Array(1);
        globalThis.crypto.getRandomValues(array);
        newMessage = messages[array[0] % messages.length];
      }
    }
    return newMessage;
  };

  return (
    <div>
      <h3 aria-live="polite">{greeting}! Thank you for visiting!</h3>
      <button onClick={() => setGreeting(randomMessage())}>
        New Greeting
      </button>
    </div>
  );
}
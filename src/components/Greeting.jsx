import { useState } from 'preact/hooks';

export default function Greeting({messages}) {

  const randomMessage = () => {
    const array = new Uint32Array(1);
    globalThis.crypto.getRandomValues(array);
    return messages[array[0] % messages.length];
  };

  const [greeting, setGreeting] = useState(messages[0]);

  return (
    <div>
      <h3>{greeting}! Thank you for visiting!</h3>
      <button onClick={() => setGreeting(randomMessage())}>
        New Greeting
      </button>
    </div>
  );
}
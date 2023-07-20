/*
    Question 2694: https://leetcode.com/problems/event-emitter/
    Nothing fancy, just do what the question asks for.
*/


class EventEmitter {
    constructor() {
        this.subscriptionDictionary = [];
    }

  subscribe(event, cb) {
    if (!(event in this.subscriptionDictionary)) {
        this.subscriptionDictionary[event] = [];
    }
    
    this.subscriptionDictionary[event].push(cb);

    return {
        unsubscribe: () => {
            this.subscriptionDictionary[event] = this.subscriptionDictionary[event].filter(callback => callback !== cb);
        }
    };
  }

  emit(event, args = []) {
      const callbacks = event in this.subscriptionDictionary ? this.subscriptionDictionary[event] : [];

      return callbacks.map(callback => callback(...args))
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
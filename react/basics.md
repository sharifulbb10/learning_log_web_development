##### What is React?

A Javascript library used to build webpages with UI components. Each UI component is a javascript function. Those are re-usable.

##### Fundamental code-snippet of React

```jsx
function MyButton() {
	// some javascript logic
	return (
		<button>Click Me!</button>
		)
}

// Now re-ues MyButton()
function MyApp() {
	// some javascript logic
	return (
		<div>
			<h2>Welcome to my app</h2>
			<MyButton />
		</div>
		)
}

// IMPORTANT
export default MyApp
```


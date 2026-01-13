##### I have a parent div tag, assgined `display: flex` css rule. Its child div tags now align horizontally. But I want its childs to align vertically when the screen shrinks. 

Solution: Add `flex-wrap: wrap` css rule to the parent. Additionally, I can set a `min-width` css property to the childs to act accordingly.

##### How to modify the styles of input box when a user is providing some input to it?

```css
input:focus {
	/*css rules*/
}
``` 

##### How to modify the blueish outline appearance of user input box during user input?
```css
input {
	outline: none; /* removes the outline */
	box-shadow: 0 0 5px grey; 

	/* box-shadow: [v-offset] [h-offset] [blur] [color] */
}
```
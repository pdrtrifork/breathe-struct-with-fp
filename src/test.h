/**
 * The Foo Struct
 */
struct Foo {
	/**
	 * Set the value.
	 *
	 * @param foo The foo.
	 * @param value The value.
	 */
    void (*SetValue)(struct Foo *foo, int value);
};


/**
 * Type definition for function that sets the value.
 *
 * @param foo The foo.
 * @param value The value.
 */
typedef void (*SetValue_t)(struct Foo *foo, int value);


/**
 * Set the value.
 *
 * @param foo The foo.
 * @param value The value.
 */
void SetValue(struct Foo *foo, int value);

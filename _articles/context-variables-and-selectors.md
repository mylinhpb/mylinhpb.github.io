---
title: "Context Variables and Selectors"
description: "Expressions in Dawiso combine static text with dynamic values to create content that automatically adapts to context."
date: 2025-12-14
tags: [Reference]
secondary_tags: [Dynamic Expressions, Automation, Notifications, Documentation]
---

{% raw %}

> The following article is the Markdown-friendly version of an article first published on the [Dawiso Help Portal](https://content.dawiso.com/data-governance/space/3/-/app/9/-/object/1164/Context-Variables-and-Selectors).

## Context variables
**Context variables**identify the source of the data. Most of these variables **must be paired with a selector to define what value to retrieve**. Examples:

- `{{currentUser}.name()}` will return the name of the user who was selected in the automation stream.
- `{{currentObject}.parent().link()}` will return a hyperlink to the parent object.
The following variables can be used for both the Notification Templates asset (type automation)and Set Attribute automation.

| **Category** | **Variable** | **Description** |
| --- | --- | --- |
| **Date** | `{currentUtcDate}` | Identifies and displays current date in ISO 8601 format (e.g., 202x-01-01). This variable **can be used on its own** or with Time Functions . |
| **Date** | `{currentUtcDateTime}` | Identifies and displays current date and time in ISO 8601 format(e.g., 202x-01-01 12:15:30) . This variable **can be used on its own**or with Time Functions . |
| **Object** | `{currentObject}` | Identifies the current object's ID. This variable can be paired with the**referenceselectors**to instead identify a**related object or user**. |
| **Object** | `{currentOrigin}` | Identifies the ID of the object that triggered the automation. Useful when streams **select**objects other than the trigger. Make sure the`keepOrigin`property in Select Streams is enabled. This variable can be paired with the**referenceselectors**to instead identify a**related object or user**. |
| **Relations** | `{relation}` | [Notifications-specific variable]**Identifies the object relation that triggered the automation.** **This variable can be paired with the**referenceselectors**to instead identify a**the target object in the relation**.** |
| **Relations** | `{userRelation}` | [Notifications-specific variable]**Identifies the user relation that was changed and triggered the automation.** |
| **User** | `{creator}` | **[Notifications-specific variable]** Identifies the user who triggered the automation. |
| **User** | `{currentUser}` | Identifies the user selected in the automation stream. |
| **User** | `{currentUserOrigin}` | Identifies the ID of the user who was assigned to the object or removed from it, triggering the automation. Useful when the user relation change triggered the automation. Make sure the `keepUserOrigin` property in Select Streams is enabled. |
| **Workflow state** | `{fromWorkflowState}` | **[Notifications-specific variable]** Identifies the starting workflow state. |
| **Workflow state**| `{toWorkflowState}` | **[Notifications-specific variable]** Identifies the ending workflow state. |
| **Other** | `{comment}` | **[Notifications-specific variable]** Identifies the comment that triggered the automation. |
| **Other** | `{constantIdPool.enum_key}` | Identifies a specific pool of IDs. Each execution of the action generates a growing numeric sequence for that key. You can define any`enum_key`. |

> [!IMPORTANT]
> Do not use `__CONCEPT_{number}` pattern in your ID pool. This pattern is reserved for object concepts, and using it elsewhere may cause concept numbering to stop working correctly.

> [!WARNING]
> Notifications-specific variables can be used only in notification templates (type automation)intended for the Send Notification automation action.

## Selectors
**Selectors**define **what information to retrieve from a context variable**. They act as a bridge between the source object (such as`{currentObject}`) and the actual data you want to use in your expression.
There are two types of selectors:

1. Reference selectors
- Reference selectors **specify a related object or user** .
- As they only point to a related object, they **must be followed by a value selector** .
- **Example** : `{currentObject}.parent().name()` = Retrieves the name of the immediate **parent** object of the current object.
1. **Value selectors**
- Value selectors **return a specific property or value** of the context variable, such as its name, ID, or link.
- They can be used directly in your output or combined with functions for additional formatting.
- **Example** : `{currentObject}.name()` = Retrieves the name of the **current object** .

### Reference selectors
Reference selectors return **a reference to an object or a user**.

> [!WARNING]
> Reference selectors only return an object reference, which is why they **must be followed by another selector to retrieve a concrete value**.
> E.g.,`{currentObject}.parent(n).name()`

| Expression | **Description** | Supported context variables |
| --- | --- | --- |
| `.parent(n)` | Identifies the **parent object** that is a specified number ( `n` ) of levels above the object. To reference the immediate parent, use `.parent()` as a shortcut for `.parent(1)` . | Objects |
| `.relation('relationTypeKey')` | Identifies the **first object** related to the object by the specified relation type ( `relationTypeKey` ). | Objects |
| `.targetObject()` | Identifies the **target object** in a relation. Can be used only with the relation variable ( `{relation}.targetObject().name()` ). | {relation} |
| `.userRelation('userRelationTypeKey')` | Identifies the **first user** related to the object by the specified user relation type ( `userRelation Type Key` ). | Objects |

These selectors can be further chained with one another, for example:

- `{currentObject}.parent().relation('core_isMentioned').name()` = Returns the name of the object related to the parent.
- `{currentObject}.parent().userRelation('core_steward').email()` = Returns the email of the steward of the parent.

### Value selectors
Value selectorsspecify**what to retrieve **from the source and **return a specific value**, such as its name, ID, or link.

| **Selector** | **Description** | Supported context variables |
| --- | --- | --- |
| `.attr('attributeKey')` | Returns the specified attribute value of an **object** . Interchangeable with `.attribute('attributeKey')` . | Objects |
| `.attribute('attributeKey')` | Returns the specified attribute value ( `attributeKey` ) of an **object** . | Objects |
| `.children()` | Returns a list of child objects. Can be combined with **array functions** . | Objects (with children) |
| `.children('objectTypeKey')` | Returns a list of child objects of the specified object type. Can be combined with **array functions** . | Objects (with children) |
| `.email()` | Returns the email address of a **user** . | Users |
| `.id()` | Returns the ID of an **object** or a **user** . | Objects/ Users |
| `.link()` | Returns a hyperlink to the selected **object** or **user** , using the asset's name as the clickable label. | Objects/ Users |
| `.link('string')` | Returns a hyperlink to the selected **object** or **user** , using the provided text as the clickable label. | Objects/ Users |
| `.name()` | Returns the name of element. | Object / Users / Relations / Workflow |
| `.pathName()` | Returns the path name of an **object** , which is also the hierarchy_name value in the database. E.g., **Parent 1/Object 1**. | Objects |
| `.relations('relationTypeKey')` | Returns a list of all target objects in the specified relation type(s). Can be combined with **array functions** . | Objects |
| `.text()` | Returns the selected **comment** 's text. | Comments |{% endraw %}

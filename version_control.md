# version\_control

## Intro

Version control is a critical part of most software development.

It allows multiple people to collaborate on massive projects and to recover old work if they need to restore or reference it. The most ubiquitous version control software is git, and we will use it for the remainder of this series.

## Git Design

In my opinion, the two major uses of version control software are:

1. To recover old versions of the project \(or parts of the project\)
2. To collaborate by working on different versions / branches of the project that will eventually get merged together.

These two use cases directly parallel two of git's exposed structures.

1. Commits
   * A commit is a snapshot of the current state of your project.
   * By looking at the commit history, a user can pick and restore old versions of their files or even their entire project.
   * This can be useful if a user wants to backtrack a bit and 'start from scratch' on a feature they've been working on.
   * Typically git users will commit after every functional change they make to a project, giving them fine-grain control over the versions of their files.
2. Branches
   1. A branch is a reference to a sequence of consecutive commits.
   2. Branches are typically used to track the development of a specific feature. For example, one might have a `maps_menu` branch which is dedicated to the development of a maps feature for their smartwatch app.
   3. Once a branch is finished, it is very common for a user to merge it back into its source \(often the primary or `main`branch\) so that the changes are incorporated back into the project.
   4. By using branches, multiple people can work on different parts / features of the overall project without stepping on each others' toes.

There is a ton more to talk about with respect to git design, but we may not have the proper tools yet to reason about it. So I will leave you with the following thought for now.

{% hint style="info" %}
 **How would you design a version control software?** 

This is a good question to come back to later when you feel like you have the tools to tackle this question. In general, it is a good learning practice to always question the standards put in front of you. By doing so, and exploring alternatives \(without reverence for the standard presented\), you will often find yourself stumbling around different designs until finding something that looks surprisingly like the original. Then your understanding will not be lectured, but discovered, due to facing the same obstacles the designers did.
{% endhint %}


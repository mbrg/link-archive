---
date: '2025-10-15'
description: '**Tensor Logic: A Unified Language for AI** This paper introduces *Tensor
  Logic*, a programming language designed to address the major limitations of existing
  AI languages. It unifies neural and symbolic AI by utilizing tensor equations, enhancing
  scalability and supporting automated reasoning. The key insight is that tensor operations
  can express both logical rules and neural network computations, enabling reliable
  reasoning in embedding spaces. Tensor Logic integrates seamlessly with existing
  frameworks, fostering transparency and learnability. This approach has implications
  for improving trust and robustness in AI applications, particularly in systems requiring
  rigorous reasoning and knowledge representation.'
link: https://arxiv.org/html/2510.12269v1
tags:
- tensor logic
- symbolic AI
- machine learning
- neural networks
- automated reasoning
title: 'Tensor Logic: The Language of AI'
---

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2510.12269v1 \[cs.AI\] 14 Oct 2025

# Tensor Logic: The Language of AI

Report issue for preceding element

\\namePedro Domingos \\emailpedrod@cs.washington.edu

\\addrPaul G. Allen School of Computer Science & Engineering

University of Washington

Seattle, WA 98195-2350, USA

Report issue for preceding element

###### Abstract

Report issue for preceding element

Progress in AI is hindered by the lack of a programming language with all the requisite features. Libraries like PyTorch and TensorFlow provide automatic differentiation and efficient GPU implementation, but are additions to Python, which was never intended for AI. Their lack of support for automated reasoning and knowledge acquisition has led to a long and costly series of hacky attempts to tack them on. On the other hand, AI languages like LISP an Prolog lack scalability and support for learning. This paper proposes tensor logic, a language that solves these problems by unifying neural and symbolic AI at a fundamental level. The sole construct in tensor logic is the tensor equation, based on the observation that logical rules and Einstein summation are essentially the same operation, and all else can be reduced to them. I show how to elegantly implement key forms of neural, symbolic and statistical AI in tensor logic, including transformers, formal reasoning, kernel machines and graphical models. Most importantly, tensor logic makes new directions possible, such as sound reasoning in embedding space. This combines the scalability and learnability of neural networks with the reliability and transparency of symbolic reasoning, and is potentially a basis for the wider adoption of AI.

Report issue for preceding element

Keywords:

deep learning, automated reasoning, knowledge representation, logic programming, Einstein summation, embeddings, kernel machines, probabilistic graphical models

Report issue for preceding element

## 1 Introduction

Report issue for preceding element

Fields take off when they find their language. Physics took off when Newton invented calculus, and couldn’t have done so without it. Maxwell’s equations would be unusable without Heaviside’s vector calculus notation. As mathematicians and physicists like to say, a good notation is half the battle. Much of electrical engineering would be impossible without complex numbers, and digital circuits without Boolean logic. Modern chip design is made possible by harware description languages, databases by relational algebra, the Internet by the Internet Protocol, and the Web by HTML. More generally, computer science would not have gotten far without high-level programming languages. Qualitative fields also depend critically on their terminology. Even artists rely on the idioms and stylistic conventions of their genre for their work.

Report issue for preceding element

A field’s language saves its practitioners time, focuses their attention, and changes how they think. It unites the field around common directions and decreases entropy. It makes key things obvious and avoids repeatedly hacking solutions from scratch.

Report issue for preceding element

Has AI found its language? LISP, one of the first high-level programming languages, made symbolic AI possible. In the 80s Prolog also became popular. Both, however, suffered from poor scalability and lack of support for learning, and were ultimately displaced, even within AI, by general-purpose languages like Java and C++. Graphical models provide a lingua franca for probabilistic AI, but their applicability is limited by the cost of inference. Formalisms like Markov logic seamlessly combine symbolic and probabilistic AI, but are also hindered by the cost of inference.

Report issue for preceding element

Python is currently the de facto language of AI, but was never designed for it, and it shows. Libraries like PyTorch and TensorFlow provide important features like automatic differentiation and GPU implementation, but are of no help for key tasks like automated reasoning and knowledge acquisition. Neurosymbolic AI seeks to ameliorate this by combining deep learning modules with symbolic AI ones, but often winds up having the shortcomings of both. In sum, AI has clearly not found its language yet.

Report issue for preceding element

There are clear desiderata for such a language. Unlike Python, it should hide everything that is not AI, allowing AI programmers to focus on what matters. It should facilitate incorporating prior knowledge into AI systems and reasoning automatically over it. It should also facilitate learning automatically, and the resulting models should be transparent and reliable. It should scale effortlessly. Symbolic AI has some of these properties and deep learning has others, but neither has all. We therefore need to merge them.

Report issue for preceding element

Tensor logic does this by unifying their mathematical foundations. It is based on the observation that essentially all neural networks can be constructed using tensor algebra, all symbolic AI using logic programming, and the two are fundamentally equivalent, differing only in the atomic data types used.

Report issue for preceding element

I begin with a brief review of logic programming and tensor algebra. The core of the paper defines tensor logic and describes its inference and learning engines. I then show how to elegantly implement neural networks, symbolic AI, kernel machines and graphical models in it. I show how tensor logic enables reliable and transparent reasoning in embedding space. I propose two approaches to scaling it up. The paper concludes with a discussion of other potential uses of tensor logic, prospects for its wide adoption, and next steps toward it.

Report issue for preceding element

## 2 Background

Report issue for preceding element

### 2.1 Logic Programming

Report issue for preceding element

The most widely used formalism in symbolic AI is logic programming (Lloyd, [1987](https://arxiv.org/html/2510.12269v1#bib.bib9 "")). The simplest logic programming language, which suffices for our purposes, is Datalog (Greco and Molinaro, [2016](https://arxiv.org/html/2510.12269v1#bib.bib4 "")). A Datalog program is a set of rules and facts. A fact is a statement of the form r​(o1,…,on)r(o\_{1},\\ldots,o\_{n}), where rr is a relation name and the oo’s are object names. For example, 𝙿𝚊𝚛𝚎𝚗𝚝​(𝙱𝚘𝚋,𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Parent(Bob,Charlie)} states that Bob is a parent of Charlie, and 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝙱𝚘𝚋){\\tt Ancestor(Alice,Bob)} that Alice is an ancestor of Bob. A rule is a statement of the form A0←A1,…,AmA\_{0}\\leftarrow A\_{1},\\ldots,A\_{m}, where the arrow means “if”, commas denote conjunction, and each of the AA’s has the form r​(x1,…,xn)r(x\_{1},\\ldots,x\_{n}), with rr being a relation name and the xx’s being variables or object names. For example, the rule

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚢)←𝙿𝚊𝚛𝚎𝚗𝚝​(𝚡,𝚢){\\tt Ancestor(x,y)}\\leftarrow{\\tt Parent(x,y)} |  |

says that parents are ancestors, and the rule

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚣)←𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚢),𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Ancestor(x,z)}\\leftarrow{\\tt Ancestor(x,y)},{\\tt Parent(y,z)} |  |

says that 𝚡{\\tt x} is 𝚣{\\tt z}’s ancestor if 𝚡{\\tt x} is 𝚢{\\tt y}’s ancestor and 𝚢{\\tt y} is 𝚣{\\tt z}’s parent. Informally, a rule says that its left-hand side or head is true if there are known facts that make all the relations on its right-hand side or body simultaneously true. For example, the rules and facts above imply that 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Ancestor(Alice,Charlie)} is true.

Report issue for preceding element

In database terminology, a Datalog rule is a series of joins followed by a projection. The (natural) join of two relations RR and SS is the set of all tuples that can be formed from tuples in RR and SS having the same values for the same arguments. When two relations have no arguments in common, their join reduces to their Cartesian product. The projection of a relation RR onto a subset GG of its arguments is the relation obtained by discarding from the tuples in RR all arguments not in GG. For example, the rule

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚣)←𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚢),𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Ancestor(x,z)}\\leftarrow{\\tt Ancestor(x,y)},{\\tt Parent(y,z)} |  |

joins the relations 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚢){\\tt Ancestor(x,y)} and 𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Parent(y,z)} on 𝚢{\\tt y} and projects the result onto {𝚡,𝚣}\\{{\\tt x},{\\tt z}\\}; the tuples 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝙱𝚘𝚋){\\tt Ancestor(Alice,Bob)} and 𝙿𝚊𝚛𝚎𝚗𝚝​(𝙱𝚘𝚋,𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Parent(Bob,Charlie)} yield the tuple 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛(𝙰𝚕𝚒𝚌𝚎,{\\tt Ancestor(Alice,}𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Charlie)}.

Report issue for preceding element

Two common inference algorithms in logic programming are forward and backward chaining. In forward chaining, the rules are repeatedly applied to the known facts to derive new facts until no further ones can be derived. The result is called the deductive closure or fixpoint of the program, and all questions of interest can be answered simply by examining it. For example, the answer to the query 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝚡){\\tt Ancestor(Alice,x)} (“Who is Alice an ancestor of?”) given the rules and facts above is {𝙱𝚘𝚋,𝙲𝚑𝚊𝚛𝚕𝚒𝚎}\\{{\\tt Bob},{\\tt Charlie}\\}.

Report issue for preceding element

Backward chaining attempts to answer a question by finding facts that match it or rules that have it as their head and facts that match the body, and so on recursively. For example, the query 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Ancestor(Alice,Charlie)} does not match any facts, but it matches the rule

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚣)←𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝚡,𝚢),𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Ancestor(x,z)}\\leftarrow{\\tt Ancestor(x,y)},{\\tt Parent(y,z)} |  |

and this rule’s body matches the facts 𝙰𝚗𝚌𝚎𝚜𝚝𝚘𝚛​(𝙰𝚕𝚒𝚌𝚎,𝙱𝚘𝚋){\\tt Ancestor(Alice,Bob)} and 𝙿𝚊𝚛𝚎𝚗𝚝​(𝙱𝚘𝚋,𝙲𝚑𝚊𝚛𝚕𝚒𝚎){\\tt Parent(Bob,Charlie)}, and therefore the answer is 𝚃𝚛𝚞𝚎{\\tt True}.

Report issue for preceding element

Forward and backward chaining in Datalog are sound inference procedures, meaning that the answers they give are guaranteed to follow logically from the rules and facts in the program. Logic programs have both declarative and procedural semantics, meaning a rule can be interpreted both as a statement about the world and as a procedure for computing its head with the given arguments by calling the procedures in the body and combining the results.

Report issue for preceding element

The field of inductive logic programming (ILP) is concerned with learning logic programs from data (Lavrač and Džeroski, [1994](https://arxiv.org/html/2510.12269v1#bib.bib7 "")). For example, an ILP system might induce the rules above from a small database of parent and ancestor relations. Once induced, these rules can answer questions about ancestry chains of any length and involving anyone. Some ILP systems can also do predicate invention, i.e., discover relations that do not appear explicitly in the data, akin to hidden variables in neural networks.

Report issue for preceding element

### 2.2 Tensor Algebra

Report issue for preceding element

A tensor is defined by two properties: its type (real, integer, Boolean, etc.) and its shape (Rabanser et al., [2017](https://arxiv.org/html/2510.12269v1#bib.bib10 "")). The shape of a tensor consists of its rank (number of indices) and its size (number of elements) along each index. For example, a video can be represented by an integer tensor of shape (t,x,y,c)(t,x,y,c), where tt is the number of frames, xx and yy are a frame’s width and height in pixels, and cc is the number of color channels (typically 3). A matrix is a rank-2 tensor, a vector a rank-1 tensor, and a scalar a rank-0 tensor. A tensor of rank rr and size nin\_{i} in the iith dimension contains a total of ∏i=1rni\\prod\_{i=1}^{r}n\_{i} elements. The element of a tensor AA at position i1i\_{1} along dimension 1, position idi\_{d} along dimension dd, etc., is denoted by Ai1,…,id,…,irA\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r}}. This generic element of a tensor is often used to represent the tensor itself. The sum of two tensors AA and BB with the same shape is a tensor CC such that

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Ci1,…,id,…,ir=Ai1,…,id,…,ir+Bi1,…,id,…,ir.C\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r}}=A\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r}}+B\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r}}. |  |

The tensor product of two tensors AA and BB of rank respectively rr and r′r^{\\prime} is a tensor CC of rank r+r′r+r^{\\prime} such that

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Ci1,…,id,…,ir,j1,…,jd′,…,jr′=Ai1,…,id,…,ir​Bj1,…,jd′,…,jr′.C\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r},j\_{1},\\ldots,j\_{d^{\\prime}},\\ldots,j\_{r^{\\prime}}}=A\_{i\_{1},\\ldots,i\_{d},\\ldots,i\_{r}}B\_{j\_{1},\\ldots,j\_{d^{\\prime}},\\ldots,j\_{r^{\\prime}}}. |  |

Einstein notation simplifies tensor equations by omitting all summation signs and implicitly summing over all repeated indices. For example, Ai​j​Bj​kA\_{ij}B\_{jk} represents the product of the matrices AA and BB, summing over jj and resulting in a matrix with indices ii and kk:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Ci​k=Ai​j​Bj​k=∑jAi​j​Bj​k.C\_{ik}=A\_{ij}B\_{jk}=\\sum\_{j}A\_{ij}B\_{jk}. |  |

More generally, the Einstein sum (or einsum for short) of two tensors AA and BB with common indices β\\beta is a tensor CC such that

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Cα​γ=∑βAα​β​Bβ​γ,C\_{\\alpha\\gamma}=\\sum\_{\\beta}A\_{\\alpha\\beta}B\_{\\beta\\gamma}, |  |

where α\\alpha, β\\beta and γ\\gamma are sets of indices, α\\alpha is the subset of AA’s indices not appearing in BB, the elements of α\\alpha and β\\beta may be interspersed in any order, and similarly for BB and γ\\gamma. Essentially all linear and multilinear operations in neural networks can be concisely expressed as einsums (Rocktäschel, [2018](https://arxiv.org/html/2510.12269v1#bib.bib11 ""); Rogozhnikov, [2022](https://arxiv.org/html/2510.12269v1#bib.bib12 "")).

Report issue for preceding element

Like matrices, tensors can be decomposed into products of smaller tensors. In particular, the Tucker decomposition decomposes a tensor into a more compact core tensor of the same rank and kkfactor matrices, each expanding an index of the core tensor into an index of the original one. For example, if AA is a rank-3 tensor, in Einstein notation its Tucker decomposition is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Ai​j​k=Mi​p​Mj​q′​Mk​r′′​Cp​q​r,A\_{ijk}=M\_{ip}M^{\\prime}\_{jq}M^{\\prime\\prime}\_{kr}C\_{pqr}, |  |

where CC is the core tensor and the MM’s are the factor matrices.

Report issue for preceding element

## 3 Tensor Logic

Report issue for preceding element

### 3.1 Representation

Report issue for preceding element

Tensor logic is based on the answers to two key questions: What is the relation between tensors and relations? And what is the relation between Datalog rules and einsums?

Report issue for preceding element

The answer to the first question is that a relation is a compact representation of a sparse Boolean tensor. For example, a social network can be represented by the neighborhood matrix Mi​jM\_{ij}, where ii and jj range over individuals and Mi​j=1M\_{ij}=1 if ii and jj are neighbors and 0 otherwise. But for large networks this is an inefficient representation, since almost all elements will be 0. The network can be more compactly represented by a relation, with a tuple for each pair of neighbors; pairs not in the relation are assumed to not be neighbors. More generally, a sparse Boolean tensor of rank nn can be compactly represented by an nn-ary relation with a tuple for each nonzero element, and the efficiency gain will typically increase exponentially with nn.

Report issue for preceding element

The answer to the second question is that a Datalog rule is an einsum over Boolean tensors, with a step function applied elementwise to the result. (Specifically, the Heaviside step function, H​(x)=1H(x)=1 if x>0x>0 and 0 otherwise.) For example, consider the rule

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚞𝚗𝚝​(𝚡,𝚣)←𝚂𝚒𝚜𝚝𝚎𝚛​(𝚡,𝚢),𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣).{\\tt Aunt(x,z)}\\leftarrow{\\tt Sister(x,y)},{\\tt Parent(y,z)}. |  |

Viewing the relations 𝙰𝚞𝚗𝚝​(𝚡,𝚣){\\tt Aunt(x,z)}, 𝚂𝚒𝚜𝚝𝚎𝚛​(𝚡,𝚢){\\tt Sister(x,y)} and 𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Parent(y,z)} as the Boolean matrices Ax​zA\_{xz}, Sx​yS\_{xy} and Py​zP\_{yz}, respectively,

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | Ax​z=H​(Sx​y​Py​z)=H​(∑ySx​y​Py​z)A\_{xz}=H(S\_{xy}P\_{yz})=H\\left(\\sum\_{y}S\_{xy}P\_{yz}\\right) |  |

will be 1 iff Sx​yS\_{xy} and Py​zP\_{yz} are both 1 for at least one yy. In other words, the einsum Sx​y​Py​zS\_{xy}P\_{yz} implements the join of 𝚂𝚒𝚜𝚝𝚎𝚛​(𝚡,𝚢){\\tt Sister(x,y)} and 𝙿𝚊𝚛𝚎𝚗𝚝​(𝚢,𝚣){\\tt Parent(y,z)}. If xx is zz’s aunt, yy is the sibling of xx who is also a parent of zz. The step function is necessary because in general for a given (x,z)(x,z) pair there may be more than one yy for which Sx​y=Py​z=1S\_{xy}=P\_{yz}=1, leading to a result greater than 1. The step function then reduces this to 1.

Report issue for preceding element

Let UU and VV be arbitrary tensors, and α\\alpha, β\\beta and γ\\gamma be sets of indices. Then Tα​γ=H​(Uα​β​Vβ​γ)T\_{\\alpha\\gamma}=H(U\_{\\alpha\\beta}V\_{\\beta\\gamma}) is a Boolean tensor whose element with indices α​γ\\alpha\\gamma is 1 when there exists some β\\beta for which Uα​β​Vβ​γ=1.U\_{\\alpha\\beta}V\_{\\beta\\gamma}=1. In other words, TT represents the join of the relations corresponding to UU and VV.

Report issue for preceding element

Since there is a direct correspondence between tensors and relations and between einsums and Datalog rules, there should also be tensor operations that directly correspond to database join and projection. We are thus led to define tensor projection and tensor join as follows.

Report issue for preceding element

The projection of a tensor TT onto a subset of its indices α\\alpha is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | πα​(T)=∑βTα​β,\\pi\_{\\alpha}(T)=\\sum\_{\\beta}T\_{\\alpha\\beta}, |  |

where β\\beta is the set of TT’s indices not in α\\alpha. (β\\beta’s elements may be interspersed with α\\alpha’s in any order.) In other words, the projection of TT onto α\\alpha is the sum for each value of α\\alpha of all the elements of TT with that value of α\\alpha. For example, a vector may be projected onto a scalar by summing all its elements, a matrix onto a column vector by summing each row into an element of the vector, a cubic tensor onto any one of its faces and then that face onto one of its edges and then onto a corner, etc. If the tensors are Boolean and the projection is followed by a step function, tensor projection reduces to database projection.

Report issue for preceding element

The join of two tensors UU and VV along a common set of indices β\\beta is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | (U⨝V)α​β​γ=Uα​β​Vβ​γ,(U\\Join V)\_{\\alpha\\beta\\gamma}=U\_{\\alpha\\beta}V\_{\\beta\\gamma}, |  |

where α\\alpha is the subset of UU’s dimensions not in VV and similarly for γ\\gamma and VV. (Again, α\\alpha, β\\beta and γ\\gamma may be interspersed in any order.) In other words, the join of two tensors on a common subset of indices β\\beta has one element for each pair of elements with the same value of β\\beta, and that element is their product. If UU has rank rr, VV has rank r′r^{\\prime}, and \|β\|=q\|\\beta\|=q, U⨝VU\\Join V has rank r+r′−qr+r^{\\prime}-q. When two tensors have no indices in common, their join reduces to their tensor product (Kronecker product for matrices). When they have all dimensions in common, it reduces to their elementwise product (Hadamard product for matrices). If the tensors are Boolean, tensor join reduces to database join.

Report issue for preceding element

A tensor logic program is a set of tensor equations. The left-hand side (LHS) of a tensor equation is the tensor being computed. The right-hand side (RHS) is a series of tensor joins followed by a tensor projection, and an optional univariate nonlinearity applied elementwise to the result. A tensor is denoted by its name followed by a list of indices, comma-separated and enclosed in square brackets. The join signs are left implicit, and the projection is onto the indices on the LHS. For example, a single-layer perceptron is implemented by the tensor equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚈=𝚜𝚝𝚎𝚙​(𝚆​\[𝚒\]​𝚇​\[𝚒\]),{\\tt Y=step(W\[i\]\\,X\[i\])}, |  |

where joining on 𝚒{\\tt i} and projecting it out implements the dot product of 𝚆{\\tt W} and 𝚇{\\tt X}. Tensors can also be specified by listing their elements, e.g., 𝚆=\[0.2,1.9,−0.7,𝟹\]{\\tt W=\[0.2,1.9,-0.7,3\]} and 𝚇=\[𝟶,𝟷,𝟷,𝟶\]{\\tt X=\[0,1,1,0\]}. Typing 𝚈​?{\\tt Y?} then causes YY to be evaluated.

Report issue for preceding element

Notice that, like the einsum implementations in NumPy, PyTorch, etc., a tensor equation is more general than the original Einstein notation: the summed-over indices are those that do not appear in the LHS, and thus a repeated index may or may not be summed over. For example, the index 𝚒{\\tt i} in

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚈​\[𝚒\]=𝚜𝚝𝚎𝚙​(𝚆​\[𝚒\]​𝚇​\[𝚒\]){\\tt Y\[i\]=step(W\[i\]\\,X\[i\])} |  |

is not summed over. The implementation of a multilayer perceptron below utilizes this.

Report issue for preceding element

Tensor elements are 0 by default, and equations with the same LHS are implicitly summed. This both preserves the correspondence with logic programming and makes tensor logic programs shorter. Tensor types may be declared or inferred. Setting a tensor equal to a file reads the file into the tensor. Reading a text file results in a Boolean matrix whose i​jijth element is 1 if the iith position in the text contains the jjth word in the vocabulary. (The matrix is not stored in this inefficient form, of course; more on this later.) For example, if the file is the string “Alice loves Bob” and it’s read into the matrix 𝙼{\\tt M}, the result is 𝙼​\[𝟶,𝙰𝚕𝚒𝚌𝚎\]=𝙼​\[𝟷,𝚕𝚘𝚟𝚎𝚜\]=𝙼​\[𝟸,𝙱𝚘𝚋\]=1{\\tt M\[0,Alice\]}={\\tt M\[1,loves\]}={\\tt M\[2,Bob\]}=1 and 𝙼​\[𝚒,𝚓\]=0{\\tt M\[i,j\]}=0 for all other 𝚒{\\tt i}, 𝚓{\\tt j}. (Notice how arbitrary constants, not just integers, can be used as indices.) Conversely, setting a file equal to a tensor writes the tensor to the file.

Report issue for preceding element

This is the entire definition of tensor logic. There are no keywords, other constructs, etc. However, it is convenient to allow some syntactic sugar that, while not increasing the expressiveness of the language, makes it more convenient to write common programs. For example, we may allow: multiple terms in one equation (e.g., 𝚈=𝚜𝚝𝚎𝚙​(𝚆​\[𝚒\]​𝚇​\[𝚒\]+𝙲){\\tt Y=step(W\[i\]\\,X\[i\]+C)}); index functions (e.g., 𝚇​\[𝚒,𝚝+𝟷\]=𝚆​\[𝚒,𝚓\]​𝚇​\[𝚓,𝚝\]{\\tt X\[i,t\\!+\\!1\]=W\[i,j\]\\,X\[j,t\]}); normalization (e.g., 𝚈​\[𝚒\]=𝚜𝚘𝚏𝚝𝚖𝚊𝚡​(𝚇​\[𝚒\]){\\tt Y\[i\]=softmax(X\[i\])}); other tensor functions (e.g., 𝚈​\[𝚔\]=𝚌𝚘𝚗𝚌𝚊𝚝​(𝚇​\[𝚒,𝚓\]){\\tt Y\[k\]=concat(X\[i,j\])}); alternate projection operators (e.g., 𝚖𝚊𝚡={\\tt max\\!=} or 𝚊𝚟𝚐={\\tt avg\\!=} instead of +⁣={\\tt+\\!=}, which ={\\tt=} defaults to); slices (e.g., 𝚇\[𝟺:𝟾\]{\\tt X\[4:8\]}); and procedural attachment (predefined or externally defined functions). Tensor logic accepts Datalog syntax; denoting a tensor with parentheses instead of square brackets implies that it’s Boolean. In particular, a sparse Boolean tensor may be written more compactly as a set of facts. For example, the vector 𝚇=\[𝟶,𝟷,𝟷,𝟶\]{\\tt X=\[0,1,1,0\]} can also be written as 𝚇​(𝟷){\\tt X(1)}, 𝚇​(𝟸){\\tt X(2)}, with 𝚇​(𝟶){\\tt X(0)} and 𝚇​(𝟹){\\tt X(3)} being implicitly 0. Similarly, reading the string “Alice loves Bob” into the matrix 𝙼{\\tt M} produces the facts 𝙼​(𝟶,𝙰𝚕𝚒𝚌𝚎){\\tt M(0,Alice)}, 𝙼​(𝟷,𝚕𝚘𝚟𝚎𝚜){\\tt M(1,loves)} and 𝙼​(𝟸,𝙱𝚘𝚋){\\tt M(2,Bob}).)

Report issue for preceding element

As another simple example, a multilayer perceptron can be implemented by the equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚇​\[𝚒,𝚓\]=𝚜𝚒𝚐​(𝚆​\[𝚒,𝚓,𝚔\]​𝚇​\[𝚒−𝟷,𝚔\]),{\\tt X\[i,j\]=sig(W\[i,j,k\]\\,X\[i\\!-\\!1,k\])}, |  |

where 𝚒{\\tt i} ranges over layers and 𝚓{\\tt j} and 𝚔{\\tt k} over units, and 𝚜𝚒𝚐​(){\\tt sig()} is the sigmoid function. Different layers may be of different sizes (and the corresponding weight matrices are implicitly padded with zeros to make up the full tensor). Alternatively, we may use a different equation for each layer.

Report issue for preceding element

A basic recursive neural network (RNN) can be implemented by

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚇\[𝚒,∗𝚝+𝟷\]=𝚜𝚒𝚐(𝚆\[𝚒,𝚓\]𝚇\[𝚓,∗𝚝\]+𝚅\[𝚒,𝚓\]𝚄\[𝚓,𝚝\]),{\\tt X\[i,\*t\\!+\\!1\]=sig(W\[i,j\]\\,X\[j,\*t\]+V\[i,j\]\\,U\[j,t\])}, |  |

where 𝚇{\\tt X} is the state, 𝚄{\\tt U} is the input, 𝚒{\\tt i} and 𝚓{\\tt j} range over units, and 𝚝{\\tt t} ranges over time steps. The ∗𝚝{\\tt\*t} notation indicates that 𝚝{\\tt t} is a virtual index: no memory is allocated for it, and successive values of the 𝚇​\[𝚒\]{\\tt X\[i\]} vector are written to the same location. Since RNNs are Turing-complete (Siegelmann and Sontag, [1995](https://arxiv.org/html/2510.12269v1#bib.bib14 "")), the implementation above implies that so is tensor logic.

Report issue for preceding element

### 3.2 Inference

Report issue for preceding element

Inference in tensor logic is carried out using tensor generalizations of forward and backward chaining.

Report issue for preceding element

In forward chaining, a tensor logic program is treated as linear code. The tensor equations are executed in turn, each one computing the tensor elements for which the necessary inputs are available; this is repeated until no new elements can be computed or a stopping criterion is satisfied.

Report issue for preceding element

In backward chaining, each tensor equation is treated as a function. The query is the top-level call, and each equation calls the equations for the tensors on its RHS until all the relevant elements are available in the data or there are no equations for the subqueries. In the latter case (sub)query elements are assigned 0 by default.

Report issue for preceding element

The choice of whether to use forward or backward chaining depends on the application.

Report issue for preceding element

### 3.3 Learning

Report issue for preceding element

Because there is only one type of statement in tensor logic—the tensor equation—automatically differentiating a tensor logic program is particularly simple. Univariate nonlinearity aside, the derivative of the LHS of a tensor equation with respect to a tensor on the RHS is just the product of the other tensors on the RHS. More precisely, if

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚈​\[…\]=𝚃​\[…\]​𝚇𝟷​\[…\]​…​𝚇𝚗​\[…\],{\\tt Y\[...\]=T\[...\]\\,X\_{1}\[...\]\\ldots X\_{n}\[...\]}, |  |

then

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | ∂𝚈​\[…\]∂𝚃​\[…\]=𝚇𝟷​\[…\]​…​𝚇𝚗​\[…\].{\\tt\\frac{\\partial Y\[...\]}{\\partial T\[...\]}=X\_{1}\[...\]\\ldots X\_{n}\[...\]}. |  |

Special cases of this include: if 𝚈=𝙰𝚇{\\tt Y=AX}, then ∂𝚈/∂𝚇=𝙰{\\tt\\partial Y/\\partial X=A}; if 𝚈=𝚆​\[𝚒\]​𝚇​\[𝚒\]{\\tt Y=W\[i\]\\,X\[i\]}, then ∂𝚈/∂𝚆​\[𝚒\]=𝚇​\[𝚒\]{\\tt\\partial Y/\\partial W\[i\]=X\[i\]}; and if 𝚈​\[𝚒,𝚓\]=𝙼​\[𝚒,𝚔\]​𝚇​\[𝚔,𝚓\]{\\tt Y\[i,j\]=M\[i,k\]\\,X\[k,j\]}, then ∂𝚈​\[𝚒,𝚓\]/∂𝙼​\[𝚒,𝚔\]=𝚇​\[𝚔,𝚓\]{\\tt\\partial Y\[i,j\]/\\partial M\[i,k\]=X\[k,j\]}.

Report issue for preceding element

As a result, the gradient of a tensor logic program is also a tensor logic program, with one equation per equation and tensor on its RHS. Omitting indices for brevity, the derivative of the loss 𝙻{\\tt L} with respect to a tensor 𝚃{\\tt T} is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | ∂𝙻∂𝚃=∑𝙴𝚍𝙻𝚍𝚈​𝚍𝚈𝚍𝚄​∏𝚄∖𝚃𝚇,{\\tt\\frac{\\partial L}{\\partial T}=\\sum\_{E}\\,\\frac{dL}{dY}\\;\\frac{dY}{dU}\\,\\prod\_{U\\setminus T}\\,X}, |  |

where 𝙴{\\tt E} are the equations whose RHSs 𝚃{\\tt T} appears in, 𝚈{\\tt Y} is the equation’s LHS, 𝚄{\\tt U} is its nonlinearity’s argument, and 𝚇{\\tt X} are the tensors in 𝚄{\\tt U}.

Report issue for preceding element

Learning a tensor logic program requires specifying the loss function and the tensors it applies to by means of one or more tensor equations. For example, to learn an MLP by minimizing squared loss on the last layer’s outputs we can use the equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙻𝚘𝚜𝚜=(𝚈\[𝚎\]−𝚇\[∗𝚎,𝙽,𝚓\])𝟸,{\\tt Loss=(Y\[e\]-X\[\*e,N,j\])^{2}}, |  |

where 𝚎{\\tt e} ranges over training examples and 𝚓{\\tt j} over units, 𝚈{\\tt Y} contains the target values, 𝚇{\\tt X} is the MLP as defined above extended with a virtual index for examples, and 𝙽{\\tt N} is the number of layers. By default, all tensors that are not supplied as training data will be learned, but the user can specify if any should remain constant (e.g., hyperparameters). The optimizer itself can be encoded in tensor logic, but typically a pre-supplied one will be used.

Report issue for preceding element

While backpropagation in traditional neural networks is applied to the same architecture for all training examples, in tensor logic the structure may effectively vary from example to example, since different equations may apply to different examples, and backpropagating through the union of all possible derivations of the example would be wasteful. Fortunately, a solution to this problem is already available in the form of backpropagation through structure, which for each example updates each equation’s parameters once for each time it appears in the example’s derivation (Goller and Küchler, [1996](https://arxiv.org/html/2510.12269v1#bib.bib3 "")). Applying this to RNNs yields the special case of backpropagation through time (Werbos, [1990](https://arxiv.org/html/2510.12269v1#bib.bib17 "")).

Report issue for preceding element

Learning a tensor logic program consisting of a fixed set of equations is quite flexible, since an equation can represent any set of rules with the same join structure. (E.g., an MLP can represent any set of propositional rules.) Further, tensor decomposition in tensor logic is effectively a generalization of predicate invention. For example, if the program to be learned is the equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰\]𝚒,𝚓,𝚔\]=𝙼\[𝚒,𝚙\]𝙼′\[𝚓,𝚚\]𝙼′′\[𝚔,𝚛\]𝙲\[𝚙,𝚚,𝚛\]{\\tt A\]i,j,k\]=M\[i,p\]\\,M^{\\prime}\[j,q\]\\,M^{\\prime\\prime}\[k,r\]\\,C\[p,q,r\]} |  |

and 𝙰{\\tt A} is the sole data tensor, the learned 𝙼{\\tt M}, 𝙼′{\\tt M^{\\prime}}, 𝙼′′{\\tt M^{\\prime\\prime}} and 𝙲{\\tt C} form a Tucker decomposition of 𝙰{\\tt A}; and thresholding them into Booleans turns them into invented predicates.

Report issue for preceding element

## 4 Implementing AI Paradigms

Report issue for preceding element

The implementations below use forward chaining unless otherwise specified.

Report issue for preceding element

### 4.1 Neural Networks

Report issue for preceding element

A convolutional neural network is an MLP with convolutional and pooling layers (LeCun et al., [1998](https://arxiv.org/html/2510.12269v1#bib.bib8 "")). A convolutional layer applies a filter at every location in an image, and can be implemented by a tensor equation of the form

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜​\[𝚡,𝚢\]=𝚛𝚎𝚕𝚞​(𝙵𝚒𝚕𝚝𝚎𝚛​\[𝚍𝚡,𝚍𝚢,𝚌𝚑\]​𝙸𝚖𝚊𝚐𝚎​\[𝚡+𝚍𝚡,𝚢+𝚍𝚢,𝚌𝚑\]),{\\tt Features\[x,y\]=relu(Filter\[dx,dy,ch\]\\,Image\[x\\!+\\!dx,y\\!+\\!dy,ch\])}, |  |

where 𝚡{\\tt x} and 𝚢{\\tt y} are pixel coordinates, 𝚍𝚡{\\tt dx} and 𝚍𝚢{\\tt dy} are filter coordinates, and 𝚌𝚑{\\tt ch} is the RGB channel. A pooling layer combines a block of nearby filters into one, and can be implemented by

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙿𝚘𝚘𝚕𝚎𝚍​\[𝚡/𝚂,𝚢/𝚂\]=𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜​\[𝚡,𝚢\],{\\tt Pooled\[x/S,y/S\]=Features\[x,y\]}, |  |

where /{\\tt/} is integer division and 𝚂{\\tt S} is the stride. This results in the filter outputs at 𝚂{\\tt S} successive positions in each dimension being summed into one. This implements sum-pooling; max-pooling would replace ={\\tt=} with 𝚖𝚊𝚡={\\tt max\\!=}, etc. A convolutional and pooling layer can be combined into one with the equation 𝙿𝚘𝚘𝚕𝚎𝚍​\[𝚡/𝚂,𝚢/𝚂\]=𝚛𝚎𝚕𝚞​(…){\\tt Pooled\[x/S,y/S\]=relu(\\ldots)}.

Report issue for preceding element

Graph neural networks (GNNs) apply deep learning to graph-structured data (e.g., social networks, molecules, metabolic networks, the Web) (Zhou, [2022](https://arxiv.org/html/2510.12269v1#bib.bib18 "")). Table [1](https://arxiv.org/html/2510.12269v1#S4.T1 "Table 1 ‣ 4.1 Neural Networks ‣ 4 Implementing AI Paradigms ‣ Tensor Logic: The Language of AI") shows the implementation of a simple GNN. The network’s graph structure is defined by the 𝙽𝚎𝚒𝚐​(𝚡,𝚢){\\tt Neig(x,y)} relation, with one fact for each adjacent (𝚡,𝚢){\\tt(x,y)} pair; or equivalently, by the Boolean tensor 𝙽𝚎𝚒𝚐​\[𝚡,𝚢\]=1{\\tt Neig\[x,y\]}=1 if 𝚡{\\tt x} and 𝚡{\\tt x} are adjacent and 0 otherwise. The main tensor is 𝙴𝚖𝚋​\[𝚗,𝚕,𝚍\]{\\tt Emb\[n,l,d\]}, containing the 𝚍{\\tt d}-dimensional embedding of each node 𝚗{\\tt n} in each layer 𝚕{\\tt l}. Initialization sets each node’s 0th-layer embeddings to its features (externally defined or learned). The network then carries out 𝙻{\\tt L} iterations of message passing, one per layer. Each iteration starts by applying one or more perceptron layers to each node. (Table [1](https://arxiv.org/html/2510.12269v1#S4.T1 "Table 1 ‣ 4.1 Neural Networks ‣ 4 Implementing AI Paradigms ‣ Tensor Logic: The Language of AI") shows one. To preserve permutation invariance, the weights 𝚆𝙿{\\tt W\_{P}} do not depend on the node. Although there are no sub/superscripts in tensor logic, I will use them here for brevity.) The GNN then aggregates each node’s neighbors’ new features 𝚉{\\tt Z} by joining the tensors 𝙽𝚎𝚒𝚐​(𝚗,𝚗′){\\tt Neig(n,n^{\\prime})} and 𝚉​\[𝚗′,𝚕,𝚍\]{\\tt Z\[n^{\\prime},l,d\]}. For each node, this zeroes out the contributions of all non-neighbors; the result is the sum of the neighbors’ features. (Internally, this can be done efficiently by iterating over the node’s neighbors or by other methods; see Section [6](https://arxiv.org/html/2510.12269v1#S6 "6 Scaling Up ‣ Tensor Logic: The Language of AI").) The aggregated features may then be passed through another MLP (not shown), after which they are combined with the node’s features using weights 𝚆𝙰𝚐𝚐{\\tt W\_{Agg}} and 𝚆𝚂𝚎𝚕𝚏{\\tt W\_{Self}} to produce the next layer’s embeddings.

Report issue for preceding element

Table 1: Graph neural networks in tensor logic

| Component | Equation |
| --- | --- |
| Graph structure | 𝙽𝚎𝚒𝚐​(𝚡,𝚢){\\tt Neig(x,y)} |
| Initialization | 𝙴𝚖𝚋​\[𝚗,𝟶,𝚍\]=𝚇​\[𝚗,𝚍\]{\\tt Emb\[n,0,d\]=X\[n,d\]} |
| MLP | 𝚉​\[𝚗,𝚕,𝚍′\]=𝚛𝚎𝚕𝚞​(𝚆𝙿​\[𝚕,𝚍′,𝚍\]​𝙴𝚖𝚋​\[𝚗,𝚕,𝚍\]){\\tt Z\[n,l,d^{\\prime}\]=relu(W\_{P}\[l,d^{\\prime},d\]\\,Emb\[n,l,d\])}, etc. |
| Aggregation | 𝙰𝚐𝚐​\[𝚗,𝚕,𝚍\]=𝙽𝚎𝚒𝚐​(𝚗,𝚗′)​𝚉​\[𝚗′,𝚕,𝚍\]{\\tt Agg\[n,l,d\]=Neig(n,n^{\\prime})\\,Z\[n^{\\prime},l,d\]} |
| Update | 𝙴𝚖𝚋​\[𝚗,𝚕+𝟷,𝚍\]=𝚛𝚎𝚕𝚞​(𝚆𝙰𝚐𝚐​𝙰𝚐𝚐​\[𝚗,𝚕,𝚍\]+𝚆𝚂𝚎𝚕𝚏​𝙴𝚖𝚋​\[𝚗,𝚕,𝚍\]){\\tt Emb\[n,l\\!+\\!1,d\]=relu(W\_{Agg}\\,Agg\[n,l,d\]+W\_{Self}\\,Emb\[n,l,d\])} |
| Node classification | 𝚈​\[𝚗\]=𝚜𝚒𝚐​(𝚆𝙾𝚞𝚝​\[𝚍\]​𝙴𝚖𝚋​\[𝚗,𝙻,𝚍\]){\\tt Y\[n\]=sig(W\_{Out}\[d\]\\,Emb\[n,L,d\])} |
| Edge prediction | 𝚈​\[𝚗,𝚗′\]=𝚜𝚒𝚐​(𝙴𝚖𝚋​\[𝚗,𝙻,𝚍\]​𝙴𝚖𝚋​\[𝚗′,𝙻,𝚍\]){\\tt Y\[n,n^{\\prime}\]=sig(Emb\[n,L,d\]\\,Emb\[n^{\\prime},L,d\])} |
| Graph classification | 𝚈=𝚜𝚒𝚐​(𝚆𝙾𝚞𝚝​\[𝚍\]​𝙴𝚖𝚋​\[𝚗,𝙻,𝚍\]){\\tt Y=sig(W\_{Out}\[d\]\\,Emb\[n,L,d\])} |

Report issue for preceding element

The most common applications of GNNs are node classification, edge prediction and graph classification. For two-class problems, each node is classified by doing the dot product of its final embedding with a weight vector, and passing the result through a sigmoid to yield the class probability. For multiclass problems (not shown), each node’s final embedding is dotted with a weight vector for each class 𝚌{\\tt c}, 𝚆𝙾𝚞𝚝​\[𝚌,𝚍\]{\\tt W\_{Out}\[c,d\]}, yielding a vector of logits that is then passed through a softmax to yield the class probabilities 𝚈​\[𝚗,𝚌\]{\\tt Y\[n,c\]}. Edge prediction predicts whether there is an edge between each pair of nodes by dotting their embeddings and passing the result through a sigmoid. Graph classification produces a class prediction for the entire graph, and is identical to node classification save for the result being a scalar 𝚈{\\tt Y} instead of a vector 𝚈​\[𝚗\]{\\tt Y\[n\]}.

Report issue for preceding element

Attention, the basis of large language models, is also straightforward to implement in tensor logic (Vaswani et al., [2017](https://arxiv.org/html/2510.12269v1#bib.bib16 "")). Given an embedding matrix 𝚇​\[𝚙,𝚍\]{\\tt X\[p,d\]}, where 𝚙{\\tt p} ranges over items (e.g., positions in a text) and 𝚍{\\tt d} over embedding dimensions, the query, key and value matrices are obtained by multiplying 𝚇{\\tt X} by the corresponding weight matrices:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚀𝚞𝚎𝚛𝚢​\[𝚙,𝚍𝚔\]=𝚆𝚀​\[𝚍𝚔,𝚍\]​𝚇​\[𝚙,𝚍\]\\displaystyle{\\tt Query\[p,d\_{k}\]=W\_{Q}\[d\_{k},d\]\\,X\[p,d\]} |  |
|  | 𝙺𝚎𝚢​\[𝚙,𝚍𝚔\]=𝚆𝙺​\[𝚍𝚔,𝚍\]​𝚇​\[𝚙,𝚍\]\\displaystyle{\\tt Key\[p,d\_{k}\]=W\_{K}\[d\_{k},d\]\\,X\[p,d\]} |  |
|  | 𝚅𝚊𝚕​\[𝚙,𝚍𝚟\]=𝚆𝚅​\[𝚍𝚟,𝚍\]​𝚇​\[𝚙,𝚍\]\\displaystyle{\\tt Val\[p,d\_{v}\]=W\_{V}\[d\_{v},d\]\\,X\[p,d\]} |  |

Attention can then be computed in two steps, the first of which compares the query at each position with each key:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙲𝚘𝚖𝚙\[𝚙,𝚙′.\]=𝚜𝚘𝚏𝚝𝚖𝚊𝚡(𝚀𝚞𝚎𝚛𝚢\[𝚙,𝚍𝚔\])𝙺𝚎𝚢\[𝚙′,𝚍𝚔\]/𝚜𝚚𝚛𝚝(𝙳𝚔)),{\\tt Comp\[p,p^{\\prime}.\]=softmax(Query\[p,d\_{k}\])\\,Key\[p^{\\prime},d\_{k}\]\\,/\\,sqrt(D\_{k}))}, |  |

where 𝚜𝚚𝚛𝚝​(𝙳𝚔){\\tt sqrt(D\_{k})} scales the dot products by the square root of the keys’ dimension. The notation 𝚙′.{\\tt p^{\\prime}.} indicates that 𝚙′{\\tt p^{\\prime}} is the index to be normalized (i.e., for each 𝚙{\\tt p}, softmax is applied to the vector indexed by 𝚙′{\\tt p^{\\prime}}). The attention head then returns the sum of the value vectors weighted by the corresponding comparisons:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙰𝚝𝚝𝚗​\[𝚙,𝚍𝚟\]=𝙲𝚘𝚖𝚙​\[𝚙,𝚙′\]​𝚅𝚊𝚕​\[𝚙′,𝚍𝚟\].{\\tt Attn\[p,d\_{v}\]=Comp\[p,p^{\\prime}\]\\,Val\[p^{\\prime},d\_{v}\]}. |  |

We can now implement an entire transformer with just a dozen tensor equations (Table [2](https://arxiv.org/html/2510.12269v1#S4.T2 "Table 2 ‣ 4.1 Neural Networks ‣ 4 Implementing AI Paradigms ‣ Tensor Logic: The Language of AI")). As we saw in Subsection [3.1](https://arxiv.org/html/2510.12269v1#S3.SS1 "3.1 Representation ‣ 3 Tensor Logic ‣ Tensor Logic: The Language of AI"), a text can be represented by the relation 𝚇​(𝚙,𝚝){\\tt X(p,t)}, stating that the 𝚙{\\tt p}th position in the text contains the 𝚝{\\tt t}th token. (Tokenization rules are easily expressed in Datalog, and are not shown.) The text’s embedding 𝙴𝚖𝚋𝚇​\[𝚙,𝚍\]{\\tt EmbX\[p,d\]} is then obtained by multiplying 𝚇​(𝚙,𝚝){\\tt X(p,t)} by the embedding matrix 𝙴𝚖𝚋​\[𝚝,𝚍\]{\\tt Emb\[t,d\]}. The next equation implements positional encoding as in the original paper (Vaswani et al., [2017](https://arxiv.org/html/2510.12269v1#bib.bib16 "")); other options are possible. (Incidentally, this equation also shows how conditionals and case statements can be implemented in tensor logic: by joining each expression with the corresponding condition.) The residual stream is then initialized to the sum of the text’s embedding and the positional encoding.

Report issue for preceding element

Table 2: Transformers in tensor logic

| Component | Equation(s) |
| --- | --- |
| Input | 𝚇​(𝚙,𝚝){\\tt X(p,t)} |
| Embedding | 𝙴𝚖𝚋𝚇​\[𝚙,𝚍\]=𝚇​(𝚙,𝚝)​𝙴𝚖𝚋​\[𝚝,𝚍\]{\\tt EmbX\[p,d\]=X(p,t)\\,Emb\[t,d\]} |
| Pos. encoding | 𝙿𝚘𝚜𝙴𝚗𝚌​\[𝚙,𝚍\]=𝙴𝚟𝚎𝚗​(𝚍)​𝚜𝚒𝚗​(𝚙/𝙻𝚍/𝙳𝚎)+𝙾𝚍𝚍​(𝚍)​𝚌𝚘𝚜​(𝚙/𝙻𝚍−𝟷/𝙳𝚎){\\tt PosEnc\[p,d\]=Even(d)\\,sin(p/L^{d/D\_{e}})+Odd(d)\\,cos(p/L^{d\\!-\\!1/D\_{e}})} |
| Residual stream | 𝚂𝚝𝚛𝚎𝚊𝚖​\[𝟶,𝚙,𝚍\]=𝙴𝚖𝚋𝚇​\[𝚙,𝚍\]+𝙿𝚘𝚜𝙴𝚗𝚌​\[𝚙,𝚍\]{\\tt Stream\[0,p,d\]=EmbX\[p,d\]+PosEnc\[p,d\]} |
| Attention | 𝚀𝚞𝚎𝚛𝚢​\[𝚋,𝚑,𝚙,𝚍𝚔\]=𝚆𝚀​\[𝚋,𝚑,𝚍𝚔,𝚍\]​𝚂𝚝𝚛𝚎𝚊𝚖​\[𝚋,𝚙,𝚍\]{\\tt Query\[b,h,p,d\_{k}\]=W\_{Q}\[b,h,d\_{k},d\]\\,Stream\[b,p,d\]}, etc. |
|  | 𝙲𝚘𝚖𝚙\[𝚋,𝚑,𝚙,𝚙′.\]=𝚜𝚘𝚏𝚝𝚖𝚊𝚡(𝚀𝚞𝚎𝚛𝚢\[𝚋,𝚑,𝚙,𝚍𝚔\]𝙺𝚎𝚢\[𝚋,𝚑,𝚙′,𝚍𝚔\]/𝚜𝚚𝚛𝚝(𝙳𝚔)){\\tt Comp\[b,h,p,p^{\\prime}.\]=softmax(Query\[b,h,p,d\_{k}\]\\,Key\[b,h,p^{\\prime},d\_{k}\]/sqrt(D\_{k}))} |
|  | 𝙰𝚝𝚝𝚗​\[𝚋,𝚑,𝚙,𝚍𝚟\]=𝙲𝚘𝚖𝚙​\[𝚋,𝚑,𝚙,𝚙′\]​𝚅𝚊𝚕​\[𝚋,𝚑,𝚙′,𝚍𝚟\]{\\tt Attn\[b,h,p,d\_{v}\]=Comp\[b,h,p,p^{\\prime}\]\\,Val\[b,h,p^{\\prime},d\_{v}\]} |
| Merge and | 𝙼𝚎𝚛𝚐𝚎​\[𝚋,𝚙,𝚍𝚖\]=𝚌𝚘𝚗𝚌𝚊𝚝​(𝙰𝚝𝚝𝚗​\[𝚋,𝚑,𝚙,𝚍𝚟\]){\\tt Merge\[b,p,d\_{m}\]=concat(Attn\[b,h,p,d\_{v}\])} |
| layer norm | 𝚂𝚝𝚛𝚎𝚊𝚖\[𝚋,𝚙,𝚍.\]=𝚕𝚗𝚘𝚛𝚖(𝚆𝚂\[𝚋,𝚍,𝚍𝚖\]𝙼𝚎𝚛𝚐𝚎\[𝚋,𝚙,𝚍𝚖\]+𝚂𝚝𝚛𝚎𝚊𝚖\[𝚋,𝚙,𝚍\]){\\tt Stream\[b,p,d.\]=lnorm(W\_{S}\[b,d,d\_{m}\]\\,Merge\[b,p,d\_{m}\]+Stream\[b,p,d\])} |
| MLP | 𝙼𝙻𝙿​\[𝚋,𝚙\]=𝚛𝚎𝚕𝚞​(𝚆𝙿​\[𝚙,𝚍\]​𝚂𝚝𝚛𝚎𝚊𝚖​\[𝚋,𝚙,𝚍\]){\\tt MLP\[b,p\]=relu(W\_{P}\[p,d\]\\,Stream\[b,p,d\])}, etc. |
| Output | 𝚈\[𝚙,𝚝.\]=𝚜𝚘𝚏𝚝𝚖𝚊𝚡(𝚆𝙾\[𝚝,𝚍\]𝚂𝚝𝚛𝚎𝚊𝚖\[𝙱,𝚙,𝚍\]){\\tt Y\[p,t.\]=softmax(W\_{O}\[t,d\]\\,Stream\[B,p,d\])} |

Report issue for preceding element

Attention is implemented as described above, with two additional indices for each tensor: 𝚋{\\tt b} for the attention block and 𝚑{\\tt h} for the attention head. The attention heads’ outputs are then concatenated, added to the residual stream and layer-normalized. MLP layers are implemented as before, with additional indices for block and position, and their outputs are also normalized and added to the stream (not shown). Finally, the output (token probabilities) is obtained by dotting the stream with an output weight vector for each token and passing through a softmax.

Report issue for preceding element

### 4.2 Symbolic AI

Report issue for preceding element

A Datalog program is a valid tensor logic program. Therefore anything that can be done in Datalog can be done in tensor logic. This suffices to implement many symbolic systems, including reasoning and planning in function-free domains. Accommodating functions (as in Prolog) requires implementing unification in tensor logic (Lloyd, [1987](https://arxiv.org/html/2510.12269v1#bib.bib9 "")).

Report issue for preceding element

### 4.3 Kernel Machines

Report issue for preceding element

A kernel machine can be implemented by the equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚈​\[𝚀\]=𝚏​(𝙰​\[𝚒\]​𝚈​\[𝚒\]​𝙺​\[𝚀,𝚒\]+𝙱),{\\tt Y\[Q\]=f(A\[i\]\\,Y\[i\]\\,K\[Q,i\]+B)}, |  |

where 𝚀{\\tt Q} is the query example, 𝚒{\\tt i} ranges over support vectors, and 𝚏​(){\\tt f()} is the output nonlinearity (e.g., a sigmoid) (Schölkopf and Smola, [2002](https://arxiv.org/html/2510.12269v1#bib.bib13 "")). The kernel 𝙺{\\tt K} is then implemented by its own equation. For example, a polynomial kernel is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙺​\[𝚒,𝚒′\]=(𝚇​\[𝚒,𝚓\]​𝚇​\[𝚒′,𝚓\])𝚗,{\\tt K\[i,i^{\\prime}\]=(X\[i,j\]\\,X\[i^{\\prime},j\])^{n}}, |  |

where 𝚒{\\tt i} and 𝚒′{\\tt i^{\\prime}} range over examples, 𝚓{\\tt j} ranges over features, and 𝚗{\\tt n} is the degree of the polynomial. A Gaussian kernel is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙺​\[𝚒,𝚒′\]=𝚎𝚡𝚙​(−(𝚇​\[𝚒,𝚓\]−𝚇​\[𝚒′,𝚓\])𝟸/𝚅𝚊𝚛).{\\tt K\[i,i^{\\prime}\]=exp(-(X\[i,j\]-X\[i^{\\prime},j\])^{2}\\,/\\,Var)}. |  |

(More precisely, 𝙺{\\tt K} is the Gram matrix of the kernel with respect to the examples.) Structured prediction, where the output consists of multiple interrelated elements (Bakr et al., [2007](https://arxiv.org/html/2510.12269v1#bib.bib1 "")), can be implemented by an output vector 𝚈​\[𝚀,𝚔\]{\\tt Y\[Q,k\]} and equations stating the interactions among outputs and between outputs and inputs.

Report issue for preceding element

### 4.4 Probabilistic Graphical Models

Report issue for preceding element

A graphical model represents the joint probability distribution of a set of random variables as a normalized product of factors,

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | P​(X=x)=1Z​∏kϕk​(x{k}),P(X\\!=\\!x)=\\frac{1}{Z}\\prod\_{k}\\phi\_{k}(x\_{\\{k\\}}), |  |

where each factor ϕk\\phi\_{k} is a non-negative function of a subset of the variables x{k}x\_{\\{k\\}} and Z=∑x∏kϕk​(x{k})Z=\\sum\_{x}\\prod\_{k}\\phi\_{k}(x\_{\\{k\\}})(Koller and Friedman, [2009](https://arxiv.org/html/2510.12269v1#bib.bib6 "")). If each factor is the conditional probability of a variable given its parents (predecessors in some partial ordering), the model is a Bayesian network and Z=1Z=1.

Report issue for preceding element

Table [3](https://arxiv.org/html/2510.12269v1#S4.T3 "Table 3 ‣ 4.4 Probabilistic Graphical Models ‣ 4 Implementing AI Paradigms ‣ Tensor Logic: The Language of AI") shows how the constructs and operations in discrete graphical models map directly onto those in tensor logic. A factor is a tensor of non-negative real values, with one index per variable and one value of the index per value of the variable. The unnormalized probability of a state xx is the product of the element in each tensor corresponding to xx. A Bayesian network can thus be encoded in tensor logic using one equation per variable, stating the variable’s distribution in terms of its conditional probability table (CPT) and the parents’ distributions:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙿𝚇​\[𝚡\]=𝙲𝙿𝚃𝚇​\[𝚡,𝚙𝚊𝚛𝟷,…,𝚙𝚊𝚛𝚗\]​𝙿𝟷​\[𝚙𝚊𝚛𝟷\]​…​𝙿𝚗​\[𝚙𝚊𝚛𝚗\].{\\tt P\_{X}\[x\]=CPT\_{X}\[x,par\_{1},...,par\_{n}\]\\,P\_{1}\[par\_{1}\]\\ldots P\_{n}\[par\_{n}\]}. |  |

Table 3: Graphical models in tensor logic

| Component | Implementation |
| --- | --- |
| Factor | Tensor |
| Marginalization | Projection |
| Pointwise product | Join |
| Join tree | Tree-like program |
| P(Query\|\|Evidence) | Prog(Q,E)/Prog(E) |
| Belief propagation | Forward chaining |
| Sampling | Selective projection |

Report issue for preceding element

Inference in graphical models is the computation of marginal and conditional probabilities, and consists of combinations of two operations: marginalization and pointwise product. The marginalization of a subset of the variables YY in a factor ϕ\\phi sums them out, leaving a factor over the remaining variables XX:

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | ϕ′​(X)=∑Yϕ​(X,Y).\\phi^{\\prime}(X)=\\sum\_{Y}\\phi(X,Y). |  |

Marginalization is just tensor projection. The pointwise product of two potentials over subsets of variables XX and YY combines them into a single potential over X∪YX\\cup Y, and is the join of the corresponding tensors.

Report issue for preceding element

Every graphical model can be expressed as a join tree, a tree of factors where each factor is a join of factors in the original model. All marginal and conditional queries can be answered in time linear in the size of the tree by successively marginalizing factors and pointwise-multiplying them with the parent’s factor. A join tree is a tree-like tensor logic program, i.e., one in which no tensor appears in more than one RHS. As a result, linear-time inference can be carried out by backward chaining over this program. Specifically: the partition function ZZ can be computed by adding the equation 𝚉=𝚃​\[…\]{\\tt Z=T\[...\]} to the program, where 𝚃​\[…\]{\\tt T\[...\]} is the LHS of the root factor’s equation, and querying 𝚉{\\tt Z}; the marginal probability of evidence P​(E)P(E) can be computed by adding EE to the program as a set of facts, querying 𝚉{\\tt Z}, and dividing by the original one; and the conditional probability of a query given evidence can be computed as P​(E)=P​(Q,E)/P​(E)P(E)=P(Q,E)/P(E).

Report issue for preceding element

However, the join tree may be exponentially larger than the original model, necessitating approximate inference. The two most popular methods are loopy belief propagation and Monte Carlo sampling. Loopy belief propagation is forward chaining on the tensor logic program representing the model. Sampling can be implemented by backward chaining with selective projection (i.e., replacing a projection by a random subset of its terms).

Report issue for preceding element

## 5 Reasoning in Embedding Space

Report issue for preceding element

The most interesting feature of tensor logic is the new models it suggests. In this section I show how to perform knowledge representation and reasoning in embedding space, and point out the reliability and transparency of this approach.

Report issue for preceding element

Consider first the case where an object’s embedding is a random unit vector. The embeddings can be stored in a matrix 𝙴𝚖𝚋​\[𝚡,𝚍\]{\\tt Emb\[x,d\]}, where 𝚡{\\tt x} ranges over objects and 𝚍{\\tt d} over embedding dimensions. Multiplying 𝙴𝚖𝚋​\[𝚡,𝚍\]{\\tt Emb\[x,d\]} by a one-hot vector 𝚅​\[𝚡\]{\\tt V\[x\]} then retrieves the corresponding object’s embedding. If 𝚅​\[𝚡\]{\\tt V\[x\]} is a multi-hot vector representing a set,

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚂​\[𝚍\]=𝚅​\[𝚡\]​𝙴𝚖𝚋​\[𝚡,𝚍\]{\\tt S\[d\]=V\[x\]\\,Emb\[x,d\]} |  |

is the superposition of the embeddings of the objects in the set. The dot product

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙳​\[𝙰\]=𝚂​\[𝚍\]​𝙴𝚖𝚋​\[𝙰,𝚍\]{\\tt D\[A\]=S\[d\]\\;Emb\[A,d\]} |  |

for some object 𝙰{\\tt A} is then approximately 1 if 𝙰{\\tt A} is in the set and approximately 0 otherwise (with standard deviation N/D\\sqrt{N/D}, where NN is the cardinality of the set and DD is the embedding dimension). Thresholding this at 12\\frac{1}{2} then tells us if 𝙰{\\tt A} is in the set with an error probability that decreases with the embedding dimension. This is similar to a Bloom filter (Bloom, [1970](https://arxiv.org/html/2510.12269v1#bib.bib2 "")).

Report issue for preceding element

The same scheme can be extended to embedding a relation. Consider a binary relation 𝚁​(𝚡,𝚢){\\tt R(x,y)} for simplicity. Then

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]=𝚁​(𝚡,𝚢)​𝙴𝚖𝚋​\[𝚡,𝚒\]​𝙴𝚖𝚋​\[𝚢,𝚓\]{\\tt EmbR\[i,j\]=R(x,y)\\,Emb\[x,i\]\\,Emb\[y,j\]} |  |

is the superposition of the embeddings of the tuples in the relation, where the embedding of a tuple is the tensor product of the embeddings of its arguments. This is a type of tensor product representation (Smolensky, [1990](https://arxiv.org/html/2510.12269v1#bib.bib15 "")). It can be computed in time linear in \|𝚁\|{\\tt\|R\|} by iterating over the tuples adding the corresponding tensor product to the result. The equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙳​\[𝙰,𝙱\]=𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]​𝙴𝚖𝚋​\[𝙰,𝚒\]​𝙴𝚖𝚋​\[𝙱,𝚓\]{\\tt D\[A,B\]=EmbR\[i,j\]\\,Emb\[A,i\]\\,Emb\[B,j\]} |  |

retrieves 𝚁​(𝙰,𝙱){\\tt R(A,B)}, i.e., 𝙳​\[𝙰,𝙱\]{\\tt D\[A,B\]} is approximately 1 if the tuple (𝙰,𝙱){\\tt(A,B)} is in the relation and 0 otherwise, since

Report issue for preceding element

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|  | 𝙳​\[𝙰,𝙱\]\\displaystyle{\\tt D\[A,B\]} | =\\displaystyle= | 𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]​𝙴𝚖𝚋​\[𝙰,𝚒\]​𝙴𝚖𝚋​\[𝙱,𝚓\]\\displaystyle{\\tt EmbR\[i,j\]\\,Emb\[A,i\]\\,Emb\[B,j\]} |  |
|  |  | =\\displaystyle= | (𝚁​(𝚡,𝚢)​𝙴𝚖𝚋​\[𝚡,𝚒\]​𝙴𝚖𝚋​\[𝚢,𝚓\])​𝙴𝚖𝚋​\[𝙰,𝚒\]​𝙴𝚖𝚋​\[𝙱,𝚓\]\\displaystyle{\\tt(R(x,y)\\,Emb\[x,i\]\\,Emb\[y,j\])\\,Emb\[A,i\]\\,Emb\[B,j\]} |  |
|  |  | =\\displaystyle= | 𝚁​(𝚡,𝚢)​(𝙴𝚖𝚋​\[𝚡,𝚒\]​𝙴𝚖𝚋​\[𝙰,𝚒\])​(𝙴𝚖𝚋​\[𝚢,𝚓\]​𝙴𝚖𝚋​\[𝙱,𝚓\])\\displaystyle{\\tt R(x,y)\\,(Emb\[x,i\]\\,Emb\[A,i\])\\,(Emb\[y,j\]\\,Emb\[B,j\])} |  |
|  |  | ≃\\displaystyle\\simeq | 𝚁​(𝙰,𝙱).\\displaystyle{\\tt R(A,B)}. |  |

The penultimate step is valid because einsums are commutative and associative. (In particular, the result does not depend on the order the tensors appear in, only on their index structure.) The last step is valid because the dot product of two random unit vectors is approximately 0.

Report issue for preceding element

By the same reasoning, the equation

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙳​\[𝙰,𝚢\]=𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]​𝙴𝚖𝚋​\[𝙰,𝚒\]​𝙴𝚖𝚋​\[𝚢,𝚓\]{\\tt D\[A,y\]=EmbR\[i,j\]\\,Emb\[A,i\]\\,Emb\[y,j\]} |  |

returns the superposition of the embeddings of the objects that are in relation 𝚁{\\tt R} to 𝙰{\\tt A}, and

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙳​\[𝚡,𝚢\]=𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]​𝙴𝚖𝚋​\[𝚡,𝚒\]​𝙴𝚖𝚋​\[𝚢,𝚓\]{\\tt D\[x,y\]=EmbR\[i,j\]\\,Emb\[x,i\]\\,Emb\[y,j\]} |  |

returns the entire relation 𝚁​(𝚡,𝚢){\\tt R(x,y)}. 𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]{\\tt EmbR\[i,j\]}, 𝙴𝚖𝚋​\[𝚡,𝚒\]{\\tt Emb\[x,i\]} and 𝙴𝚖𝚋​\[𝚢,𝚓\]{\\tt Emb\[y,j\]} form a Tucker decomposition of the data tensor 𝙳​\[𝚡,𝚢\]{\\tt D\[x,y\]}, with 𝙴𝚖𝚋𝚁​\[𝚒,𝚓\]{\\tt EmbR\[i,j\]} as the core tensor and 𝙴𝚖𝚋​\[𝚡,𝚒\]{\\tt Emb\[x,i\]} and 𝙴𝚖𝚋​\[𝚢,𝚓\]{\\tt Emb\[y,j\]} as the factor matrices.

Report issue for preceding element

The relation symbols themselves may be embedded. (E.g., 𝚁{\\tt R}, 𝙰{\\tt A} and 𝙱{\\tt B} in 𝚁​(𝙰,𝙱){\\tt R(A,B)} may all be embedded.) This results in a rank-3 tensor. Relations of arbitrary arity can be reduced to sets of (relation, argument, value) triples. Thus an entire database can be embedded as a single rank-3 tensor.

Report issue for preceding element

The next step is to embed rules. We can embed a Datalog rule by replacing its antecedents and consequents by their embeddings: if the rule is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙲𝚘𝚗𝚜​(…)←𝙰𝚗𝚝𝟷​(…),…,𝙰𝚗𝚝𝚗​(…),{\\tt Cons(...)\\leftarrow Ant\_{1}(...),\\ldots,Ant\_{n}(...)}, |  |

its embedding is

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙴𝚖𝚋𝙲𝚘𝚗𝚜​\[…\]=𝙴𝚖𝚋𝙰𝚗𝚝𝟷​\[…\]​…​𝙴𝚖𝚋𝙰𝚗𝚝𝚗​\[…\],{\\tt EmbCons\[...\]=EmbAnt\_{1}\[...\]\\ldots EmbAnt\_{n}\[...\]}, |  |

where

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝙴𝚖𝚋𝙰𝚗𝚝𝟷​\[…\]=𝙰𝚗𝚝𝟷​(…)​𝙴𝚖𝚋​\[…\]​…​𝙴𝚖𝚋​\[…\],{\\tt EmbAnt\_{1}\[...\]=Ant\_{1}(...)\\,Emb\[...\]\\ldots Emb\[...\]}, |  |

etc. Reasoning in embedding space can now be carried out by forward or backward chaining over the embedded rules. The answer to a query can be extracted by joining its tensor with its arguments’ embeddings, as shown above for any relation. This gives approximately the correct result because each inferred tensor can be expressed as a sum of projections of joins of embedded relations, and the product 𝙴𝚖𝚋​\[𝚡,𝚒\]​𝙴𝚖𝚋​\[𝚡′,𝚒\]{\\tt Emb\[x,i\]\\,Emb\[x^{\\prime},i\]} for each of its arguments is approximately the identity matrix. The error probability decreases with the embedding dimension, as before. To further reduce it, we can extract, threshold and re-embed the inferred tensors at regular intervals (in the limit, after each rule application).

Report issue for preceding element

The most interesting case, however, is when objects’ embeddings are learned. The product of the embedding matrix and its transpose,

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | 𝚂𝚒𝚖​\[𝚡,𝚡′\]=𝙴𝚖𝚋​\[𝚡,𝚍\]​𝙴𝚖𝚋​\[𝚡′,𝚍\],{\\tt Sim\[x,x^{\\prime}\]=Emb\[x,d\]\\,Emb\[x^{\\prime},d\]}, |  |

is now the Gram matrix measuring the similarity of each pair of objects by the dot product of their embeddings. Similar objects “borrow” inferences from each other, with weight proportional to their similarity. This leads to a powerful form of analogical reasoning that explicitly combines similarity and compositionality in a deep architecture.

Report issue for preceding element

If we apply a sigmoid to each equation,

Report issue for preceding element

|     |     |     |
| --- | --- | --- |
|  | σ​(x,T)=1(1+e−x/T),\\sigma(x,T)=\\frac{1}{(1+e^{-x/T})}, |  |

setting its temperature parameter TT to 0 effectively reduces the Gram matrix to the identity matrix, making the program’s reasoning purely deductive. This contrasts with LLMs, which may hallucinate even at T=0T=0. It’s also exponentially more powerful than retrieval-augmented generation (Jiang et al., [2025](https://arxiv.org/html/2510.12269v1#bib.bib5 "")), since it effectively retrieves the deductive closure of the facts under the rules rather than just the facts.

Report issue for preceding element

Increasing the temperature makes reasoning increasingly analogical, with examples that are less and less similar borrowing inferences from each other. The optimal TT will depend on the application, and can be different for different rules (e.g., some rules may be mathematical truths and have T=0T=0, while others may serve to accumulate weak evidence and have a high TT).

Report issue for preceding element

The inferred tensors can be extracted at any point during inference. This makes reasoning highly transparent, in contrast with LLM-based reasoning models. It’s also highly reliable and immune to hallucinations at sufficiently low temperature, again in contrast with LLM-based models. At the same time, it has the generalization and analogical abilities of reasoning in embedding space. This could make it ideal for a wide range of applications.

Report issue for preceding element

## 6 Scaling Up

Report issue for preceding element

For large-scale learning and inference, equations involving dense tensors can be directly implemented on GPUs. Operations on sparse and mixed tensors can be implemented using (at least) one of two approaches.

Report issue for preceding element

The first is separation of concerns: operations on dense (sub)tensors are implemented on GPUs, and operations on sparse (sub)tensors are implemented using a database query engine, by treating (sub)tensors as relations. The full panoply of query optimization can then be applied to combining these sparse (sub)tensors. An entire dense subtensor may be treated as single tuple by the database engine, with an argument pointing to the subtensor. Dense subtensors are then joined and projected using GPUs.

Report issue for preceding element

The second and more interesting approach is to carry out all operations on GPUs, first converting the sparse tensors into dense ones via Tucker decomposition. This is exponentially more efficient than operating directly on the sparse tensors, and as we saw in the previous section, even a random decomposition will suffice. The price is that there will be a small probability of error, but this can be controlled by appropriately setting the embedding dimension and denoising results by passing them through step functions. Scaling up via Tucker decompositions has the significant advantage that it combines seamlessly with the learning and reasoning algorithms described in previous sections.

Report issue for preceding element

## 7 Discussion

Report issue for preceding element

Tensor logic is likely to be useful beyond AI. Scientific computing consists essentially of translating equations into code, and with tensor logic this translation is more direct than with previous languages, often with a one-to-one correspondence between symbols on paper and symbols in code. In scientific computing the relevant equations are then wrapped in logical statements that control their execution. Tensor logic makes this control structure automatically learnable by relaxing the corresponding Boolean tensors to numeric ones, and optionally thresholding the results back into logic. The same approach is applicable in principle to making any program learnable.

Report issue for preceding element

Any new programming language faces a steep climb to wide adoption. What are tensor logic’s chances of succeeding? AI programming is no longer a niche; tensor logic can ride the AI wave to wide adoption in the same way that Java rode the Internet wave. Backward compatibility with Python is key, and tensor logic lends itself well to it: it can initially be used as a more elegant implementation of einsum and extension of Python to reasoning tasks, and as it develops it can absorb more and more features of NumPy, PyTorch, etc., until it supersedes them.

Report issue for preceding element

Above all, adoption of new languages is driven by the big pains they cure and the killer apps they support, and tensor logic very much has these: e.g., it potentially cures the hallucinations and opacity of LLMs, and is the ideal language for reasoning, mathematical and coding models.

Report issue for preceding element

Fostering an open-source community around tensor logic will be front and center. Tensor logic lends itself to IDEs that tightly integrate coding, data wrangling, modeling and evaluation, and if it takes off vendors will compete to support it. It is also ideally suited to teaching and learning AI, and this is another vector by which it can spread.

Report issue for preceding element

Next steps include implementing tensor logic directly in CUDA, using it in a wide range of applications, developing libraries and extensions, and pursuing the new research directions it makes possible.

Report issue for preceding element

For more information on tensor logic, visit tensor-logic.org.

Report issue for preceding element

Acknowledgments

Report issue for preceding element

This research was partly funded by ONR grant N00014-18-1-2826.

Report issue for preceding element

## References

Report issue for preceding element

- Bakr et al. (2007)↑
G. Bakr, T. Hofmann, B. Schölkopf, A. Smola, B. Taskar, and S. Vishwanathan,
editors.

_Predicting Structured Data_.

MIT Press, Cambridge, MA, 2007.

- Bloom (1970)↑
B. Bloom.

Space/time tradeoffs in hash coding with allowable errors.

_Comm. ACM_, 13:422–426, 1970.

- Goller and Küchler (1996)↑
C. Goller and A. Küchler.

Learning task-dependent distributed representations by
backpropagation through structure.

In _Proc. Int. Conf. Neural Networks_, pp. 347–352, 1996.

- Greco and Molinaro (2016)↑
S. Greco and C. Molinaro.

_Datalog and Logic Databases_.

Morgan & Claypool, San Rafael, CA, 2016.

- Jiang et al. (2025)↑
P. Jiang, S. Ouyang, Y. Jiao, M. Zhong, R. Tian, and J. Han.

Retrieval and structuring augmented generation with large language
models.

In _Proc. Int. Conf. Knowl. Disc. & Data Mining_, pp.
6032–6042, 2025.

- Koller and Friedman (2009)↑
D. Koller and N. Friedman.

_Probabilistic Graphical Models: Principles and Techniques_.

MIT Press, Cambridge, MA, 2009.

- Lavrač and Džeroski (1994)↑
N. Lavrač and S. Džeroski.

_Inductive Logic Programming: Techniques and Applications_.

Ellis Horwood, Chichester, UK, 1994.

- LeCun et al. (1998)↑
Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner.

Gradient-based learning applied to document recognition.

_Proc. IEEE_, 86:2278–2324, 1998.

- Lloyd (1987)↑
J. W. Lloyd.

_Foundations of Logic Programming_ (2nd ed.).

Springer, Berlin, Germany, 1987.

- Rabanser et al. (2017)↑
S. Rabanser, O. Shchur, and S. Günnemann.

Introduction to tensor decompositions and their applications in
machine learning.

arXiv:1711.1078, 2017.

- Rocktäschel (2018)↑
T. Rocktäschel.

Einsum is all you need – Einstein summation in deep learning.

https://rockt.ai/2018/04/30/einsum, 2018.

- Rogozhnikov (2022)↑
A. Rogozhnikov.

Einops: Clear and reliable tensor manipulations with Einstein-like
notation.

In _Proc. Int. Conf. Learn. Repr._, 2022.

- Schölkopf and Smola (2002)↑
B. Schölkopf and A. J. Smola.

_Learning with Kernels: Support Vector Machines, Regularization,_
_Optimization, and Beyond_.

MIT Press, Cambridge, MA, 2002.

- Siegelmann and Sontag (1995)↑
H. Siegelmann and E. Sontag.

On the computational power of neural nets.

_J. Comp. & Sys. Sci._, 50:132–150, 1995.

- Smolensky (1990)↑
P. Smolensky.

Tensor product variable binding and the representation of symbolic
structures in connectionist systems.

_Artif. Intel._, 46:159–216, 1990.

- Vaswani et al. (2017)↑
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. Gomez, L. Kaiser,
and I. Polosukhin.

Attention is all you need.

_Adv. Neural Inf. Proc. Sys._, 30:5998–6008, 2017.

- Werbos (1990)↑
P. Werbos.

Backpropagation through time: What it does and how to do it.

_Proc. IEEE_, 78:1550–1560, 1990.

- Zhou (2022)↑
Z. Liu & J. Zhou.

_Introduction to Graph Neural Networks_.

Morgan & Claypool, San Rafael, CA, 2022.


Report IssueReport Issue for Selection

Generated by
[L\\
A\\
T\\
Exml![[LOGO]](<Base64-Image-Removed>)](https://math.nist.gov/~BMiller/LaTeXML/)

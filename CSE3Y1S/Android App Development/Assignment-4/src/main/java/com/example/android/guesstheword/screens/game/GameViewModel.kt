package com.example.android.guesstheword.screens.game

import  android.lyfecycle.LiveData
import  android.lyfecycle.MutableLiveData
import android.lifecycle.ViewModel


class GameViewModel : ViewModel(){

    // The current word
   private val  word =MutableLiveData<String>()
    val word:Livedata<String>
    get() = _word


    // The current score
     private val score = MutableLiveData<Int>()
     val score:Livedata<Int>
     get() = _score


    // The list of words - the front of the list is the next word to guess
    private lateinit var wordList: MutableList<String>

    / Event which triggers the end of the game
    private val _eventGameFinish = MutableLiveData<Boolean>()
    val eventGameFinish: LiveData<Boolean>
        get() = _eventGameFinish

    init {
        resetList()
        nextWord()
        _score.value=0

    }
    /**
     * Resets the list of words and randomizes the order
     */
    private fun resetList() {
        wordList = mutableListOf(
            "queen",
            "hospital",
            "basketball",
            "cat",
            "change",
            "snail",
            "soup",
            "calendar",
            "sad",
            "desk",
            "guitar",
            "home",
            "railway",
            "zebra",
            "jelly",
            "car",
            "crow",
            "trade",
            "bag",
            "roll",
            "bubble"
        )
        wordList.shuffle()
    }
    /**
     * Moves to the next word in the list
     */
    private fun nextWord() {
        //Select and remove a word from the list
        if (wordList.isEmpty()) {
            _eventGameFinish.value = true
        } else {
            _word = wordList.removeAt(0)
        }

    }

    /** Methods for buttons presses **/

    fun onSkip() {
        _score.value = (_score.value)?.minus(1)
        nextWord()
    }

  fun onCorrect() {
        _score.value =(_score.value)?plus(1)
        nextWord()
    }
    /** Methods for completed events **/
    fun onGameFinishComplete() {
        _eventGameFinish.value = false
    }
}